// src/echo.ts
// Ce fichier est désactivé car nous utilisons Tauri IPC pour le temps réel.
const mockEcho = {
    channel: () => ({ listen: () => { } }),
    private: () => ({ listen: () => { } }),
    leave: () => { },
};
export default mockEcho;
