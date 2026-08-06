import Container from "../ui/Container";

import HeaderLogo from "./HeaderLogo";
import HeaderNav from "./HeaderNav";
import HeaderActions from "./HeaderActions";
import SearchBar from "../search/SearchBar";

export default function Header() {
  return (
    <header
      style={{
        borderBottom: "1px solid #eee",
        padding: "18px 0",
      }}
    >
      <Container>
        <div
          style={{
            display: "flex",
            justifyContent: "space-between",
            alignItems: "center",
            gap: 24,
          }}
        >
          <HeaderLogo />

          <HeaderNav />

          <SearchBar />

          <HeaderActions />
        </div>
      </Container>
    </header>
  );
}
