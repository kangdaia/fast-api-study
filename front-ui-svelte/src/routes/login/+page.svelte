<script>

</script>

<div class="flex justify-center">
<div class="text-white rounded-lg py-8 px-10 flex flex-col bg-zinc-700 justify-self-center self-center min-w-[420px]">
    <h1 class="p-2.5 text-xl text-center font-bold">로그인</h1>
    <form method="POST" class="grid grid-col align-center gap-2.5 my-2.5">
		<label class="grid grid-row gap-2 ">
			<b>Username</b>
			<input class="bg-zinc-800 p-2 rounded-lg"
				name="username"
				autocomplete="off"
			/>
		</label>
        <label class="grid grid-row gap-2">
			<b>비밀번호</b>
			<input class="bg-zinc-800 p-2 rounded-lg"
				name="password"
				type="password"
			/>
		</label>
        <button type="submit" class="bg-zinc-600 rounded-lg px-5 py-2 flex-shrink my-2.5">로그인</button>
	</form>
</div>
</div>