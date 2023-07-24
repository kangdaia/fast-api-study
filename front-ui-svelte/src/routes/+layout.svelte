<script>
    import "../app.css";
</script>
<nav class="p-5 flex flex-row text-white gap-5">
    <!-- svelte-ignore missing-declaration -->
    <a class="px-5 py-2 rounded-lg bg-zinc-600" href="/">Home</a>
    <a class="px-5 py-2 rounded-lg bg-zinc-600" href="/signup">회원가입</a>
    <a class="px-5 py-2 rounded-lg bg-zinc-600" href="/login">로그인</a>
</nav>
<slot />
