import Link from "next/link";


const links = [
  {href : "/docs" , label : "Docs"},
  {href : "/todos" , label : "Todos"},
  {href : "/" , label : "Home"}
]
export default function Home() {
  return (
    <>
    <div>Welcome to homePage</div>

    {links.map((link)=>{
      return(
        <Link key={link.href} href={link.href}>{link.label}</Link>
      )
    })}
    </>
  );
}
