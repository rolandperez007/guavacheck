"use client";

import {
  ResponsiveContainer,
  BarChart,
  Bar,
  XAxis,
  YAxis,
  Tooltip
} from "recharts";

interface ROIChartProps {
  data: any[];
}

export default function ROIChart({
  data
}: ROIChartProps) {
  return (
    <div className="h-80 w-full">
      <ResponsiveContainer width="100%" height="100%">
        <BarChart data={data}>
          <XAxis dataKey="title" />
          <YAxis />
          <Tooltip />
          <Bar dataKey="roi" />
        </BarChart>
      </ResponsiveContainer>
    </div>
  );
}


