import React, { useEffect, useState } from "react";
import { View, Text, FlatList, TouchableOpacity } from "react-native";

const API = "http://localhost:3000/api/mobile/austin";

export default function App() {
  const [feed, setFeed] = useState<any[]>([]);
  const [mode, setMode] = useState("dashboard");

  useEffect(() => {
    loadDashboard();
  }, []);

  async function loadDashboard() {
    const res = await fetch(API, {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({
        action: "dashboard",
        user: { id: "mobile_user" },
      }),
    });

    const json = await res.json();
    setFeed(json.feed || []);
  }

  async function runForecast(item: any) {
    const res = await fetch(API, {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({
        action: "forecast",
        property: item,
      }),
    });

    const json = await res.json();
    alert("Forecast: " + JSON.stringify(json));
  }

  async function analyze(item: any) {
    const res = await fetch(API, {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({
        action: "analyze",
        property: item,
        user: { id: "mobile_user" },
      }),
    });

    const json = await res.json();
    alert("AI Analysis: " + JSON.stringify(json.decision));
  }

  return (
    <View style={{ padding: 20, marginTop: 50 }}>
      <Text style={{ fontSize: 22, fontWeight: "bold" }}>🏦 Austin Investor App</Text>

      <Text style={{ marginVertical: 10 }}>🌍 Global Property Intelligence Feed</Text>

      <FlatList
        data={feed}
        keyExtractor={(item, i) => i.toString()}
        renderItem={({ item }) => (
          <View
            style={{
              padding: 15,
              borderWidth: 1,
              marginBottom: 10,
              borderRadius: 10,
            }}
          >
            <Text style={{ fontWeight: "bold" }}>{item.title}</Text>

            <Text>{item.location}</Text>
            <Text>₦{item.price}</Text>

            <View style={{ flexDirection: "row", marginTop: 10 }}>
              <TouchableOpacity onPress={() => analyze(item)}>
                <Text style={{ color: "blue", marginRight: 15 }}>AI Analyze</Text>
              </TouchableOpacity>

              <TouchableOpacity onPress={() => runForecast(item)}>
                <Text style={{ color: "green" }}>Forecast</Text>
              </TouchableOpacity>
            </View>
          </View>
        )}
      />
    </View>
  );
}
