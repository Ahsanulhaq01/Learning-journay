import mongoose from "mongoose";

const todoSchema = mongoose.Schema({
    content: {
        type: String,

    },
    createdBy: {
        type: String,
        default: "ahsan"
    }
})

export default mongoose.model.Todo || mongoose.model("Todo", todoSchema);