import React from 'react';

import { ToastContainer, toast } from 'react-toastify';
import 'react-toastify/dist/ReactToastify.css';

const successNotify = () => toast.success("Successfully.");
const errorNotify = () => toast.error("Some error happend,please try again !")

const SuccessToast = () => {
    return (
        <> 
            {successNotify()}
            <ToastContainer
                position="top-left"
                autoClose={2000}
                hideProgressBar={false}
                newestOnTop={false}
                closeOnClick
                rtl={false}
                pauseOnFocusLoss
                draggable
                pauseOnHover
                theme="light"
            />
        </>
    );
}

const ErrorToast = () => {
    return (
        <>
            {errorNotify()}
            <ToastContainer
                position="top-left"
                autoClose={2000}
                hideProgressBar={false}
                newestOnTop={false}
                closeOnClick
                rtl={false}
                pauseOnFocusLoss
                draggable
                pauseOnHover
                theme="light"
            />
        </>
    );
}


export {
    SuccessToast,
    ErrorToast
};