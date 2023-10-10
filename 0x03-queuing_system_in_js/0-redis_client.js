import { createClient } from "redis";

async function connectToRedis() {
  try {
    const client = await createClient();

    client.on('connect', () => console.log('Redis client connected to the server'));
    client.on('error', err => console.log(`Redis client not connected to the server: ${err}`));
  } catch (error) {
    console.error('Error connecting to Redis: ', error);
  }
}
connectToRedis();
