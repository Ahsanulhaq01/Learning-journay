import Link from "next/link";

async function delay(ms){
   return await new Promise((resolve)=>{
    setTimeout(resolve , ms)
  })

 
}

async function getLinks(){
  await delay(2000);
   return  [
  {href : "/docs" , label : "Docs"},
  {href : "/todos" , label : "Todos"},
  {href : "/" , label : "Home"}
]
}

export default async function Home() {

  const links = await getLinks();
  return (
    <>
    <div>Welcome to homePage</div>
    <hr/>
    {links.map((link)=>{
      return(
        <Link key={link.href} href={link.href}>{link.label}</Link>
      )
    })}
    </>
  );
}
