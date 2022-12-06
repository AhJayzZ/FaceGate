import axios from "axios";

const API = 'http://127.0.0.1:8000/api/';

const getData = async() => {
    try{
        const res = await axios.get(API);
        return res
    }
    catch (error){
        console.log(error);
        return error
    }
}

const getDataById = async(id) => {
    try{
        const res = await axios.get(API + String(id));
        return res
    }
    catch (error){
        console.log(error);
        return error
    }
}

const postData = async(data) => {
    try{
        const res = await axios.post(API,data);
        return res
    }
    catch (error) {
        console.log(error);
        return error
    }
}

const putData = async(data) => {
    try{
        const res = await axios.put(API,data);
        return res
    }
    catch (error) {
        console.log(error);
        return error
    }
}

const deleteData = async(id) => {
    try{
        const res = await axios.delete(API + String(id));
        return res
    }
    catch (error) {
        console.log(error);
        return error
    }
}

export {
    getData,
    getDataById,
    postData,
    putData,
    deleteData
}