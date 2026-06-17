import { PrismaClient } from "@/app/generated/prisma";

let prisma;

let globalForPrisma = global;

if(process.env.NODE_ENV === 'production'){
    prisma = new PrismaClient()
}
else{
    if(!globalForPrisma.prisma){
        globalForPrisma.prisma = new PrismaClient()
    }

    prisma = globalForPrisma.prisma
}

export default prisma