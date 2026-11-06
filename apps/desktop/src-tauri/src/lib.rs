use std::net::{SocketAddr, TcpStream};
use std::path::PathBuf;
use std::process::{Child, Command};
use std::sync::Mutex;
use std::time::Duration;

use tauri::{Manager, RunEvent};

const GATEWAY: &str = "127.0.0.1:8010";

struct Backend(Mutex<Option<Child>>);

/// Radice del repo: risaliamo finché troviamo il supervisore dei servizi.
fn repo_root() -> Option<PathBuf> {
    let mut starts = Vec::new();
    if let Ok(cwd) = std::env::current_dir() {
        starts.push(cwd);
    }
    if let Ok(exe) = std::env::current_exe() {
        if let Some(dir) = exe.parent() {
            starts.push(dir.to_path_buf());
        }
    }
    starts.into_iter().find_map(|start| {
        let mut dir = Some(start);
        while let Some(current) = dir {
            if current.join("scripts").join("stack.py").is_file() {
                return Some(current);
            }
            dir = current.parent().map(PathBuf::from);
        }
        None
    })
}

fn gateway_running() -> bool {
    let Ok(address) = GATEWAY.parse::<SocketAddr>() else {
        return false;
    };
    TcpStream::connect_timeout(&address, Duration::from_millis(250)).is_ok()
}

fn spawn_backend() -> Option<Child> {
    let root = repo_root()?;
    Command::new("python")
        .args(["scripts/stack.py", "--dev", "--no-sync"])
        .current_dir(root)
        .spawn()
        .ok()
}

/// Su Windows `kill` termina solo il supervisore: serve l'intero albero.
fn stop_backend(child: &mut Child) {
    #[cfg(windows)]
    {
        let _ = Command::new("taskkill")
            .args(["/PID", &child.id().to_string(), "/T", "/F"])
            .status();
    }
    #[cfg(not(windows))]
    {
        let _ = child.kill();
        let _ = child.wait();
    }
}

#[cfg_attr(mobile, tauri::mobile_entry_point)]
pub fn run() {
    tauri::Builder::default()
        .manage(Backend(Mutex::new(None)))
        .setup(|app| {
            // Se il gateway risponde, i servizi sono già attivi: non ne avviamo altri.
            if !gateway_running() {
                if let Some(child) = spawn_backend() {
                    if let Some(state) = app.try_state::<Backend>() {
                        *state.0.lock().expect("lock backend") = Some(child);
                    }
                }
            }
            Ok(())
        })
        .build(tauri::generate_context!())
        .expect("avvio di Noesis Studio fallito")
        .run(|app, event| {
            if let RunEvent::Exit = event {
                if let Some(state) = app.try_state::<Backend>() {
                    if let Some(mut child) = state.0.lock().expect("lock backend").take() {
                        stop_backend(&mut child);
                    }
                }
            }
        });
}
