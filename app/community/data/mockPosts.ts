import { CommunityPost } from "../types/community";

export const posts: CommunityPost[] = [
  {
    id: 1,
    author: "Michael A.",
    role: "Architect",
    category: "Architecture",
    title: "Should modern homes still include courtyards?",
    excerpt:
      "Clients are increasingly requesting naturally ventilated homes. Are courtyards making a comeback?",
    replies: 24,
    likes: 118,
    time: "2 hours ago",
  },
  {
    id: 2,
    author: "Grace O.",
    role: "Builder",
    category: "Construction",
    title: "Foundation costs increased unexpectedly",
    excerpt: "What strategies are helping reduce excavation costs without compromising quality?",
    replies: 17,
    likes: 91,
    time: "Today",
  },
  {
    id: 3,
    author: "Daniel K.",
    role: "Engineer",
    category: "Materials",
    title: "Roofing sheets for coastal environments",
    excerpt: "Looking for corrosion-resistant roofing options for humid climates.",
    replies: 31,
    likes: 204,
    time: "Yesterday",
  },
];
