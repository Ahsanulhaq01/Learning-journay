import mongoose from "mongoose";


async function connectDB() {
    try {
       await mongoose.connect(process.env.DATABASE_URL);
       console.log("DataBase Connected !")
    } catch (error) {
        throw new Error("DB Connection failed");
    }
}

export default connectDB;