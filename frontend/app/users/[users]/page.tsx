import React from "react";
import {BackEnd_URL} from "@/config/url";
import {CardUser} from "@/components/card";
import {revalidateTag} from 'next/cache'

async function getUsers(user_id: number) {

    const res = await fetch(`${BackEnd_URL}/users/best_results/${user_id}/`, {
        method: 'GET',
        headers: {
            'bypass-tunnel-reminder': 'true',
            'User-Agent': 'Custom',
            'cache': "no-store",
            'ngrok-skip-browser-warning': 'true', // Встановлюємо заголовок для уникнення повідомлення про браузер
            'Cache-Control': 'no-store, max-age=0'
        },
        cache: 'no-store'
    })
    // The return value is *not* serialized
    // You can return Date, Map, Set, etc.

    if (!res.ok) {
        // This will activate the closest `error.js` Error Boundary
        throw new Error('Failed to fetch data')
    }

    return res.json()
}

// eslint-disable-next-line @next/next/no-async-client-component
export default async function UsersPage({params}: any) {
    const usersData = await getUsers(params.users)
    const users = await usersData['data']


    if ((users)) {
        return (

            <div>
                {users.map((user: any, index: number) => {

                    return (
                        // eslint-disable-next-line react/jsx-key
                        <CardUser index={index} param={params} user={user}/>
                    )
                })
                }
            </div>
        )
    } else {
        return <h1 className="mt-20 mb-6 text-large font-bold leading-none text-default-600">Unfortunately, we have not
            found the right people for you. Try changing your profile parameters...</h1>
    }
}