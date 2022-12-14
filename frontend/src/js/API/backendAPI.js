import axios from "axios";

const API_ROOT = process.env.REACT_APP_NGORK_URL
const GET_URL = API_ROOT + "/api/item/getalldate"
const READ_URL = API_ROOT + "/api/item/read/"
const POST_URL = API_ROOT  + "/api/item/create"
const PUT_URL = API_ROOT + "/api/item/update/"

const getData = async() => {
    try{
        console.log(API_ROOT,GET_URL)
        const res = await axios.get(GET_URL);
        return res
    }
    catch (error){
        console.log(error);
        return error
    }
}

const getDataByName = async(id) => {
    try{
        const res = await axios.get(READ_URL + String(id));
        return res
    }
    catch (error){
        console.log(error);
        return error
    }
}

const postData = async(data) => {
    try{

        const res = await axios.post(POST_URL,data);
        return res
    }
    catch (error) {
        console.log(error);
        return error
    }
}

const putData = async(data) => {
    try{
        const res = await axios.put(PUT_URL,data);
        return res
    }
    catch (error) {
        console.log(error);
        return error
    }
}

export {
    getData,
    getDataByName,
    postData,
    putData
}