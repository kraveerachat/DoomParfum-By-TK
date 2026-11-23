# Node 24.22.3 (LTS) on Alpine 3.24, pinned by multi-arch index digest.
FROM node:24.22.3-alpine3.24@sha256:116b800c3754b440ee0aa3ed2f20f5bf3d99a554bfd9adeea09ea8017f6e85f5 AS base
ENV NEXT_TELEMETRY_DISABLED=1
WORKDIR /app

FROM base AS deps
COPY package.json package-lock.json .npmrc ./
RUN npm ci --ignore-scripts

# Development target: the source is bind-mounted by compose.dev.yaml.
FROM deps AS dev
RUN mkdir -p .next && chown node:node /app .next
USER node
EXPOSE 3000
CMD ["npm", "run", "dev"]

FROM deps AS builder
COPY . .
RUN npm run typecheck:gen && npm run lint && npm test && npm run build
RUN find .next/standalone .next/static -name "*.map" -not -path "*/node_modules/*" -delete

FROM base AS runner
ENV NODE_ENV=production PORT=3000 HOSTNAME=0.0.0.0
# The runtime needs only node; remove package managers from the image.
RUN rm -rf /usr/local/lib/node_modules /usr/local/bin/npm /usr/local/bin/npx /usr/local/bin/corepack /usr/local/bin/yarn* /opt/yarn*
COPY --from=builder --chown=root:root /app/.next/standalone ./
COPY --from=builder --chown=root:root /app/.next/static ./.next/static
COPY --from=builder --chown=root:root /app/public ./public
COPY --from=builder --chown=root:root /app/scripts/healthcheck.mjs ./healthcheck.mjs
COPY --from=builder --chown=root:root /app/NOTICE.md ./NOTICE.md
COPY --from=builder --chown=root:root /app/src/fonts/OFL-BodoniModa.txt /app/src/fonts/OFL-NotoSansThai.txt ./licenses/
USER node
EXPOSE 3000
HEALTHCHECK --interval=15s --timeout=4s --start-period=10s --retries=3 CMD ["node", "healthcheck.mjs"]
CMD ["node", "server.js"]
