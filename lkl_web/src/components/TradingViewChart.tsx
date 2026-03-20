import { useEffect, useRef } from 'react';
import { createChart, ColorType } from 'lightweight-charts';

interface TradingViewChartProps {
    symbol: string;
    data?: any[];
    height?: number;
}

export default function TradingViewChart({ symbol, data = [], height = 300 }: TradingViewChartProps) {
    const chartContainerRef = useRef<HTMLDivElement>(null);

    useEffect(() => {
        if (!chartContainerRef.current) return;

        const chart = createChart(chartContainerRef.current, {
            layout: {
                background: { type: ColorType.Solid, color: '#0a0a0a' },
                textColor: '#d1d4dc',
            },
            grid: {
                vertLines: { color: 'rgba(255, 255, 255, 0.05)' },
                horzLines: { color: 'rgba(255, 255, 255, 0.05)' },
            },
            width: chartContainerRef.current.clientWidth,
            height: height,
            timeScale: {
                timeVisible: true,
                secondsVisible: false,
            },
        });

        const candlestickSeries = chart.addCandlestickSeries({
            upColor: '#10b981',
            downColor: '#ef4444',
            borderVisible: false,
            wickUpColor: '#10b981',
            wickDownColor: '#ef4444',
        });

        // If real data is provided, use it. Otherwise, generate sample data for demo
        if (data && data.length > 0) {
            candlestickSeries.setData(data);
        } else {
            // Generate sample candlestick data for demonstration
            const sampleData = generateSampleData();
            candlestickSeries.setData(sampleData);
        }

        chart.timeScale().fitContent();

        const handleResize = () => {
            if (chartContainerRef.current) {
                chart.applyOptions({ width: chartContainerRef.current.clientWidth });
            }
        };

        window.addEventListener('resize', handleResize);

        return () => {
            window.removeEventListener('resize', handleResize);
            chart.remove();
        };
    }, [data, height, symbol]);

    return (
        <div
            ref={chartContainerRef}
            style={{
                position: 'relative',
                width: '100%',
                height: `${height}px`,
                background: '#0a0a0a',
            }}
        />
    );
}

// Generate sample candlestick data for demonstration
function generateSampleData() {
    const data = [];
    const basePrice = 1800 + Math.random() * 200;
    let currentPrice = basePrice;
    const now = Math.floor(Date.now() / 1000);

    for (let i = 100; i >= 0; i--) {
        const time = now - i * 3600; // 1 hour intervals
        const change = (Math.random() - 0.5) * 20;
        const open = currentPrice;
        const close = currentPrice + change;
        const high = Math.max(open, close) + Math.random() * 10;
        const low = Math.min(open, close) - Math.random() * 10;

        data.push({
            time: time,
            open: parseFloat(open.toFixed(2)),
            high: parseFloat(high.toFixed(2)),
            low: parseFloat(low.toFixed(2)),
            close: parseFloat(close.toFixed(2)),
        });

        currentPrice = close;
    }

    return data;
}
