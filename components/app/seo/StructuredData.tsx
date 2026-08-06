import {
  organizationSchema,
  softwareSchema,
} from "@/app/seo/schema";

export default function StructuredData() {
  return (
    <script
      type="application/ld+json"
      dangerouslySetInnerHTML={{
        __html: JSON.stringify([
          organizationSchema(),
          softwareSchema(),
        ]),
      }}
    />
  );
}