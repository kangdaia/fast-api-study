<script>
    import fastapi from "../../lib/fastapi"
    import { page } from "../../lib/store"
    import { onMount } from 'svelte';

    let music_list = [];
    let limit = 30
    let total = 0
    $: total_page = Math.ceil(total/limit)

    async function get_music_list(_page) {
        let params = {
            page: _page,
            limit: limit,
        }
        fastapi('get', '/api/musics/list', params, (json) => {
            music_list = json.tracks
            $page = json.page
            limit = json.size
        }, ()=>{console.log("fail")})
    }
    onMount(async () => {
        get_music_list($page)
    })
</script>

<div>
    <h1 class="text-3xl font-bold text-white p-5">
        Top Track
    </h1>
    <ul class="p-5 flex flex-col gap-2">
        {#if music_list}
        {#each music_list as music}
            <div class="text-lg text-white flex flex-row align-center">
                <img class="rounded-lg" src={music.image[1]["#text"]} alt={music.image[1]["size"]}/>
                <div class="flex flex-col px-2 justify-center">
                    <div class="font-bold">{music.name}</div>
                    <p class="text-sm">{music.artist.name}</p>
                </div>
            </div>
        {/each}
        {/if}
    </ul>
    <ul class="pagination justify-content-center">
        <!-- 이전페이지 -->
        <li class="page-item {$page <= 0 && 'disabled'}">
            <button class="page-link" on:click="{() => get_music_list($page-1)}">이전</button>
        </li>
        <!-- 페이지번호 -->
        {#each Array(total_page) as _, loop_page}
        {#if loop_page >= $page-5 && loop_page <= $page+5} 
            <li class="page-item {loop_page === $page && 'active'}">
                <button on:click="{() => get_music_list(loop_page)}" class="page-link">{loop_page+1}</button>
            </li>
        {/if}
        {/each}
        <!-- 다음페이지 -->
        <li class="page-item {$page >= total_page-1 && 'disabled'}">
            <button class="page-link" on:click="{() => get_music_list($page+1)}">다음</button>
        </li>
    </ul>
</div>