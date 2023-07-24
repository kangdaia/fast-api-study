<script>
    import Error from '../../components/Error.svelte';
    export let form;
	let error = {detail:[]};

	async function post_user(event) {
		const data = new FormData(this);
		let url = "/api/user/signup"
		let params = {
			user_create: {
				username: data.get("username"),
				email: data.get("email"),
				password1: data.get("password1"),
				password2: data.get("password2")
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
</script>

<div class="flex justify-center">
<div class="text-white rounded-lg py-8 px-10 flex flex-col bg-zinc-700 justify-self-center self-center min-w-[420px]">
    <h1 class="p-2.5 text-xl text-center font-bold">회원가입</h1>
    <form method="post" on:submit|preventDefault={post_user} class="grid grid-col align-center gap-2.5 my-2.5">
        {#if form?.success}
            <Error error={form.error}/>
        {/if}
        <label class="grid grid-row gap-2 ">
			<b>Username</b>
			<input class="bg-zinc-800 p-2 rounded-lg"
				name="username"
                id="username" 
			/>
		</label>
        <label class="grid grid-row gap-2 ">
			<b>Email</b>
			<input class="bg-zinc-800 p-2 rounded-lg"
				name="email"
				id="email" 
                type="email"
			/>
		</label>
        <label class="grid grid-row gap-2">
			<b>비밀번호</b>
			<input class="bg-zinc-800 p-2 rounded-lg"
				name="password1"
				type="password"
                id="password1" 
			/>
		</label>
        <label class="grid grid-row gap-2">
			<b>비밀번호 확인</b>
			<input class="bg-zinc-800 p-2 rounded-lg"
				name="password2"
				type="password"
                id="password2" 
			/>
		</label>
        <button type="submit" class="bg-zinc-600 rounded-lg px-5 py-2 flex-shrink my-2.5">가입하기</button>
	</form>
</div>
</div>