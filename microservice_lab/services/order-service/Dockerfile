FROM node:20-alpine

WORKDIR /app
COPY package.json ./
RUN npm install --omit=dev
COPY server.js ./
COPY data ./data

EXPOSE 3003
CMD ["npm", "start"]

