FROM denoland/deno:latest as base
EXPOSE 8080
WORKDIR /app
USER deno
COPY . .
RUN deno cache main.ts
RUN mkdir -p /var/tmp/log
CMD ["run", "--allow-all", "main.ts"] 
