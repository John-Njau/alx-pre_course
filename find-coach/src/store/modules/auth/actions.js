import axios from 'axios';

export default {
    login(){},
    async signup(context, payload){
        const response = await fetch('', {
            method: 'POST',
            body: JSON.stringify({
                email: payload.email,
                password: payload.password,
                returnSecureToken: true
            })
        });

        const responseData = await response.json();

        if (!response.ok){
            const error = new Error(responseData.message || 'Failed to authenticate');
            throw error;
        }

        console.log(responseData);
    }
};