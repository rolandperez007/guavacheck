import { redirect } from "next/navigation";

export const metadata = {
  title: "guavacheck | The Future of the Built Environment",
  description:
    "Building the Future of the Built Environment. Powered by Austin.",
};

export default function HomePage() {
  redirect("/gateway");
}