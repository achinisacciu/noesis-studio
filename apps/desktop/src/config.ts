import { ApiClient } from "./api";

const gatewayUrl = import.meta.env.VITE_GATEWAY_URL ?? "http://127.0.0.1:8010";
const token = import.meta.env.VITE_NOESIS_TOKEN ?? "dev-token";

export const client = new ApiClient(gatewayUrl, token);
export const gatewayLabel = gatewayUrl;
