# Visual Vision - Open License Media Search Web Application

## Overview
Visual Vision is a comprehensive web application designed for searching and managing openly-licensed media from the Openverse API. This project was developed as part of the CMP9134 Software Engineering module at the University of Lincoln.

## Key Features
- **User Account Management**
  - Secure registration and authentication system
  - Saved search history management
  - Profile customization options

- **Media Search Interface**
  - Integration with Openverse API for CC-licensed content
  - Advanced search filters (media type, license, size, etc.)
  - Media preview and display functionality

- **Technical Implementation**
  - Modular architecture following MVC pattern
  - Containerized deployment with Docker
  - Automated testing and CI/CD pipeline
  - Responsive frontend design

## Technologies Used
- **Frontend**: React.js with Material-UI
- **Backend**: Node.js/Express
- **Database**: MongoDB
- **DevOps**: Docker, GitHub Actions
- **Testing**: Jest, React Testing Library

## Installation Guide

### Prerequisites
- Docker and Docker Compose installed
- Node.js (v16 or later)
- MongoDB (or use the Dockerized version)

### Setup Instructions
1. Clone the repository:
   ```bash
   git clone https://github.com/j0rdan0x006/Visual-Vision.git
   cd Visual-Vision
   ```

2. Set up environment variables:
   - Create `.env` files in both `client` and `server` directories based on the provided `.env.example` files

3. Run with Docker:
   ```bash
   docker-compose up --build
   ```

4. Access the application at `http://localhost:3000`

### Alternative Local Development Setup
1. Install dependencies:
   ```bash
   cd server && npm install
   cd ../client && npm install
   ```

2. Start the development servers:
   - In one terminal:
     ```bash
     cd server && npm run dev
     ```
   - In another terminal:
     ```bash
     cd client && npm start
     ```

