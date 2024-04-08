"use client"
import React, {useState} from "react";
import {HeartIcon} from '@/components/HeartIcon';
import {Card, CardHeader, CardBody, CardFooter, Button, Link, Image} from "@nextui-org/react";
import {HeartIconFill} from "@/components/HeartIconFill";
import {BackEnd_URL} from "@/config/url";


async function getData(user_id: number) {

    const res = await fetch(`${BackEnd_URL}/user/${user_id}`, {
        headers: {
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

async function getUserLike(from_user: number, to_user: number) {

    const res = await fetch(`${BackEnd_URL}/get/likes/${from_user}/${to_user}`, {
        headers: {
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


// eslint-disable-next-line @next/next/no-async-client-component
export default async function Page({params}: any) {
    const data = await getData(params.about)
    const get_like = await getUserLike(params.users, params.about)

    // @ts-ignore
    const LikeButton = ({user_id}) => {
        const [liked, setLiked] = useState(!!get_like.data);

        const handleLikeClick = () => {
            setLiked(!liked);

            if (liked) {
                const res = fetch(`${BackEnd_URL}/remove/like/${params.users}/${user_id}`, {
                    headers: {
                        'ngrok-skip-browser-warning': 'true'
                    }
                })
            } else {
                const res = fetch(`${BackEnd_URL}/add/like/${params.users}/${user_id}`, {
                    headers: {
                        'ngrok-skip-browser-warning': 'true'
                    }
                })
            }
        };


        // @ts-ignore
        return <Button isIconOnly color="danger" variant="faded" aria-label="Like"
                       className="float-right" onPress={handleLikeClick}>
            {liked ? <HeartIconFill filled={undefined} size={undefined} height={undefined} width={undefined}
                                    label={undefined}/> :
                <HeartIcon filled={undefined} size={undefined} height={undefined} width={undefined} label={undefined}/>}
        </Button>;
    };

    return (
        <div>
            <h1 className="mt-20 mb-6 text-large font-bold leading-none text-default-600"> {data.data.name}</h1>
            <Card className="py-4 mt-6">
                <CardHeader className="pb-0 pt-2 px-4 items-start justify-between">
                    <div className="flex gap-5">
                        <div className="flex flex-col gap-1 items-start justify-center">
                            <h4 className="text-large font-semibold leading-none text-default-600">{data.data.name},</h4>
                            <small className="text-default-500">{data.data.age}</small>
                            <h4 className="text-small font-semibold leading-none text-default-600">{data.data.city}</h4>
                        </div>
                        <div className="flex flex-col gap-1 items-start justify-center">
                            <h5 className="text-small tracking-tight text-default-400"></h5>
                        </div>
                    </div>
                    <LikeButton user_id={data.data.telegram_id}/>
                </CardHeader>
                <CardBody className="overflow-visible py-2 items-center justify-center">
                    <Image
                        isZoomed
                        isBlurred
                        alt="Card background"
                        className="object-cover rounded-xl items-center justify-center"
                        src={data.data.photo} // Використовуйте фото з API
                        width={270}
                    />
                </CardBody>
                <CardFooter>
                    <p className="text-small font-semibold text-default-400">
                        {data.data.about}
                    </p>
                </CardFooter>
            </Card>
            <Button
                href={`/users/${params.users}`}
                as={Link}
                color="danger"
                fullWidth={true}
                variant="flat"
                size="md"
                className="mt-4"
            >
                <h4 className="text-medium font-semibold leading-none text-default-600">Go back</h4>
            </Button>
        </div>
    )
}
