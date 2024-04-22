import React, {Suspense} from "react";
import {HeartIcon} from '@/components/HeartIcon';
import {Card, CardHeader, CardBody, CardFooter} from "@nextui-org/card";
import {Button} from "@nextui-org/button"
import {Image} from "@nextui-org/image"
import {HeartIconFill} from "@/components/HeartIconFill";
import {Link} from "@nextui-org/link";
import {BackEnd_URL} from "@/config/url";
import {LikeButton} from "@/components/LikeButton";
import Loading from "@/app/users/[users]/[about]/loading";
import {CardAboutUser} from "@/components/card_about";
import {revalidateTag} from "next/cache";


async function getData(user_id: number) {

    const res = await fetch(`${BackEnd_URL}/users/id/${user_id}`, {
        method: 'GET',
        headers: {
            'bypass-tunnel-reminder': 'true',
            'User-Agent': 'Custom',
            'cache': "no-store",
            'Cache-Control': 'no-store, max-age=0',
            'ngrok-skip-browser-warning': 'true' // Встановлюємо заголовок для уникнення повідомлення про браузер
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
export default async function Page({params}: any) {
    const data = await getData(params.about)

    return (
        <div>
            <h1 className="mt-20 mb-6 text-large font-bold leading-none text-default-600"> {data.data.name}</h1>
            <CardAboutUser data={data} index={0} params={params}/>
        </div>
    )
}