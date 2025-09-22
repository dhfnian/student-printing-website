# Frontend - Vite React
FROM node:20-alpine AS deps
WORKDIR /app
COPY package.json package-lock.json* pnpm-lock.yaml* yarn.lock* ./
RUN npm ci --ignore-scripts || npm install --no-audit --no-fund
COPY . .
RUN npm run build

FROM node:20-alpine AS runner
WORKDIR /app
COPY --from=deps /app/dist ./dist
RUN npm i -g serve
EXPOSE 5173
CMD ["serve","-s","dist","-l","5173"]
