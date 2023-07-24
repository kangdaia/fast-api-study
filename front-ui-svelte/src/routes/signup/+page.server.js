import { json } from '@sveltejs/kit'
import fastapi from '$lib/fastapi'

export const actions = {
    default: async ({ request }) => {
        const formData = await request.formData();
        const username = formData.get('username');
        const email = formData.get('email');
        const password1 = formData.get('password1');
        const password2 = formData.get('password2');
        let error = {detail:[]}
        function post_user() {
            let url = "/api/user/signup"
            let params = {
                user_create: {
                    username: username,
                    email: email,
                    password1: password1,
                    password2: password2,
                }
            }
            fastapi('post', url, params, 
                (json) => {
                    push('/login')
                },
                (json_error) => {
                    error = json_error
                }
            )
        }
        //console.log(formData);
        post_user();
        return {
            success: true,
            formData,
            error
        };
    }
};