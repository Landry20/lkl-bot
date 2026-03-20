// src/App.tsx
import { BrowserRouter, Routes, Route } from "react-router-dom";
import Dashboard from "./components/Dashboard";
import Positions from "./components/Positions";
import Announce from "./components/Announce";
import Archives from "./components/Archives";
import Register from "./components/Register";
import ErrorPage from "./components/ErrorPage";
import ToastContainer from "./components/ToastContainer";
import InstallBanner from "./components/InstallBanner";
import { useState, useEffect } from "react";

import Login from "./components/Login";
import MainLayout from "./components/MainLayout";
import ForgotPassword from "./components/ForgotPassword";

import TradingTerminal from "./components/TradingTerminal";
import Occasions from "./components/Occasions";
import Settings from "./components/Settings";
import ChatIA from "./components/ChatIA";
import EconomicNews from "./components/EconomicNews";
import Markets from "./components/Markets";
import Analyses from "./components/Analyses";
import MacroGeo from "./components/MacroGeo";

const GuardedRoute = ({ children }: { children: React.ReactNode }) => {
  const token = localStorage.getItem("token");
  if (!token) {
    return <Login />;
  }
  return <>{children}</>;
};

export default function App() {
  const [errorState, setErrorState] = useState<{ status: number, message: string } | null>(null);

  useEffect(() => {
    const handleApiError = (event: any) => {
      setErrorState(event.detail);
    };
    window.addEventListener('api-error', handleApiError);
    return () => window.removeEventListener('api-error', handleApiError);
  }, []);

  if (errorState) {
    return (
      <ErrorPage
        status={errorState.status}
        message={errorState.message}
        onRetry={() => {
          setErrorState(null);
          window.location.reload();
        }}
      />
    );
  }

  return (
    <>
      <InstallBanner />
      <ToastContainer />
      <BrowserRouter>
        <Routes>
          <Route path="/login" element={<Login />} />
          <Route path="/register" element={<Register />} />
          <Route path="/forgot-password" element={<ForgotPassword />} />

          <Route element={<GuardedRoute><MainLayout /></GuardedRoute>}>
            <Route path="/" element={<Dashboard />} />
            <Route path="/positions" element={<Positions />} />
            <Route path="/announce" element={<Announce />} />
            <Route path="/archives" element={<Archives />} />

            {/* New Routes */}
            <Route path="/chat-ia" element={<ChatIA />} />
            <Route path="/occasions" element={<Occasions />} />
            <Route path="/trading-terminal" element={<TradingTerminal />} />
            <Route path="/settings" element={<Settings />} />
            <Route path="/economic-news" element={<EconomicNews />} />
            <Route path="/markets" element={<Markets />} />
            <Route path="/analyses" element={<Analyses />} />
            <Route path="/macro-geo" element={<MacroGeo />} />
          </Route>
        </Routes>
      </BrowserRouter>
    </>
  );
}