import Link from "next/link";

interface Item {
  name: string;
  href: string;
}

interface Props {
  items: Item[];
}

export default function Breadcrumbs({
  items,
}: Props) {
  return (
    <nav aria-label="Breadcrumb">
      <ol
        style={{
          display: "flex",
          gap: 10,
          listStyle: "none",
          padding: 0,
          margin: "20px 0",
        }}
      >
        {items.map((item, index) => (
          <li key={item.href}>
            <Link href={item.href}>{item.name}</Link>

            {index < items.length - 1 && " / "}
          </li>
        ))}
      </ol>
    </nav>
  );
}