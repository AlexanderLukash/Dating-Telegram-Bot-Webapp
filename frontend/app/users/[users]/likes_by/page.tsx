'use client'
import React from "react";
import {Button, Card, CardBody, CardFooter, CardHeader, Image, Link} from "@nextui-org/react";
import {BackEnd_URL} from "@/config/url";


async function getUserData(user_id: number) {

    const res = await fetch(`${BackEnd_URL}/user/${user_id}/`, {
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

async function getLikes(user_id: number) {

    const res = await fetch(`${BackEnd_URL}/get/likes/to/${user_id}`, {
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
export default async function UsersPage({params}: any) {
    const userData = await getUserData(params.users)
    const usersLikesData = await getLikes(userData.data.telegram_id)
    const users = await usersLikesData['data']

    if (users) {
        return (
            <div>
                {users.map((user: {
                    name: string;
                    age: number;
                    city: string;
                    username: string;
                    photo: string;
                    telegram_id: number;
                }) => {

                    return (
                        // eslint-disable-next-line react/jsx-key
                        <Card className="py-4 mb-6 mt-6">
                            <CardHeader className="pb-0 pt-2 px-4 items-start justify-between">
                                <div className="flex gap-5">
                                    <div className="flex flex-col gap-1 items-start justify-center">
                                        <h4 className="text-large font-semibold leading-none text-default-600">{user.name},</h4>
                                        <small className="text-default-500">{user.age}</small>
                                    </div>
                                    <div className="flex flex-col gap-1 items-start justify-center">
                                        <h5 className="text-small tracking-tight text-default-400"></h5>
                                    </div>
                                </div>
                                <h4 className="text-small font-semibold leading-none text-default-600">{user.city}</h4>
                            </CardHeader>
                            <CardBody className="overflow-visible py-2 items-center justify-center">
                                <Image
                                    isZoomed
                                    isBlurred
                                    alt={user.username}
                                    className="object-cover rounded-xl items-center justify-center"
                                    src={user.photo} // Використовуйте фото з API
                                    width={270}
                                />
                            </CardBody>
                            <CardFooter className="gap-3 -mt-2 -mb-2 px-3 py-0 text-small text-default-400">
                                <Button
                                    href={`/users/${params.users}/${user.telegram_id}`}
                                    as={Link}
                                    color="danger"
                                    fullWidth={true}
                                    variant="flat"
                                    size="md"
                                    className="mt-4"
                                >
                                    <h4 className="text-medium font-semibold leading-none text-default-600">Read
                                        more</h4>
                                </Button>
                            </CardFooter>
                        </Card>
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
