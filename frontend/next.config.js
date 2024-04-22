/** @type {import('next').NextConfig} */

require('dotenv').config({ path: '../.env' });
const nextConfig = {
        env: {
            BACKEND_URL: process.env.BACKEND_URL,
        },
    }

module.exports = nextConfig

