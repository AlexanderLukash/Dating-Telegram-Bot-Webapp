import {BackEnd_URL} from "@/config/url";

export async function getUserLike(from_user: number, to_user: number) {

    const res = await fetch(`${BackEnd_URL}/likes/get/${from_user}/${to_user}`, {
        method: 'GET',
        headers: {
            'bypass-tunnel-reminder': 'true',
            'User-Agent': 'Custom',
            'ngrok-skip-browser-warning': 'true' // Встановлюємо заголовок для уникнення повідомлення про браузер
        }
    })
    // The return value is *not* serialized
    // You can return Date, Map, Set, etc.

    if (!res.ok) {
        // This will activate the closest `error.js` Error Boundary
        throw new Error('Failed to fetch data')
    }

    return res.json()
}
