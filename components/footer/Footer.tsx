import Container from "../ui/Container";

export default function Footer() {
  return (
    <footer
      style={{
        borderTop: "1px solid #eee",
        marginTop: 80,
        padding: "40px 0",
      }}
    >
      <Container>
        © {new Date().getFullYear()} Guava Networks 
      </Container>
    </footer>
  );
}