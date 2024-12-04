import { serve } from "https://deno.land/std@0.182.0/http/server.ts"

// const PORT = 8000;
// const server = serve({ PORT });

const PORT = 8000;
const server = serve({ port: PORT });

console.log(`Listening on http://localhost:${PORT}/`);

for await (const req of server) {
	req.respond({ body: "Hi! Welcome to the Deno world. Smiles" });
}
