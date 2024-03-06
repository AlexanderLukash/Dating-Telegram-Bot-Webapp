import {title} from "@/components/primitives";
import React from "react";
import {Card, CardHeader, CardBody, Image} from "@nextui-org/react";

async function getData() {
    const res = await fetch('http://127.0.0.1:8000/user/1')
    // The return value is *not* serialized
    // You can return Date, Map, Set, etc.

    if (!res.ok) {
        // This will activate the closest `error.js` Error Boundary
        throw new Error('Failed to fetch data')
    }

    return res.json()
}

export default async function AboutPage() {
    const data = await getData()

    return (
        <div>
            <h1 className={title()}>About</h1>
            <Card className="py-4">
                <CardHeader className="pb-0 pt-2 px-4 flex-col items-start">
                    <p className="text-tiny uppercase font-bold">{data.name}</p>
                    <small className="text-default-500">{data.age}</small>
                    <h4 className="font-bold text-large">{data.city}</h4>
                </CardHeader>
                <CardBody className="overflow-visible py-2">
                    <Image
                        alt="Card background"
                        className="object-cover rounded-xl"
                        src="https://cdn.discordapp.com/attachments/1163358305385730121/1209834469050290218/image.png?ex=65e85d27&is=65d5e827&hm=f7f698cf1578024ce2fb132bf43a7ffc67353dbaf5f4e906e26b08c10c0a317a&"
                        width={270}
                    />
                </CardBody>
            </Card>
        </div>
    )
        ;
}
