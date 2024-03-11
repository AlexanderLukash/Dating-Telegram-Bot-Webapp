import {title} from "@/components/primitives";
import React from "react";
import {HeartIcon} from '@/components/HeartIcon';
import {Card, CardHeader, CardBody, CardFooter, Button, Image} from "@nextui-org/react";

async function getData() {
    const res = await fetch('http://127.0.0.1:8000/users')
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
        <section className="flex flex-col items-center justify-center gap-4 py-8 md:py-10">

            <h1 className={title()}>Анкети для вас</h1>
            <div>
                <Card className="py-4">
                    <CardHeader className="pb-0 pt-2 px-4 flex-col items-start">
                        <div className="flex gap-5">
                            <div className="flex flex-col gap-1 items-start justify-center">
                                <h4 className="text-large font-semibold leading-none text-default-600">{data.name}, {data.age}</h4>
                                <h4 className="text-small font-semibold leading-none text-default-600">{data.city}</h4>
                            </div>
                            <div className="flex flex-col gap-1 items-start justify-center">
                                <h5 className="text-small tracking-tight text-default-400"></h5>
                            </div>
                            <div className="flex flex-col gap-1 items-start justify-center">

                                <Button isIconOnly color="danger" variant="faded" aria-label="Like"
                                        className="ml-20 -mr-2">
                                    <HeartIcon filled={undefined} size={undefined} height={undefined} width={undefined}
                                               label={undefined}/>
                                </Button>
                            </div>
                        </div>
                    </CardHeader>
                    <CardBody className="overflow-visible py-2">
                        <Image
                            alt="Card background"
                            className="object-cover rounded-xl"
                            src="https://cdn.discordapp.com/attachments/1163358305385730121/1209834469050290218/image.png?ex=65e85d27&is=65d5e827&hm=f7f698cf1578024ce2fb132bf43a7ffc67353dbaf5f4e906e26b08c10c0a317a&"
                            width={270}
                        />
                    </CardBody>
                    <CardFooter className="gap-3 -mt-2 -mb-2 px-3 py-0 text-small text-default-400">
                        <p>
                            {data.about}
                        </p>
                    </CardFooter>
                </Card>
            </div>
        </section>)
        ;
}
