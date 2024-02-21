import {title} from "@/components/primitives";
import React from "react";
import {Card, CardHeader, CardBody, Image} from "@nextui-org/react";

export default function AboutPage() {
    return (
        <div>
            <h1 className={title()}>About</h1>
            <Card className="py-4">
                <CardHeader className="pb-0 pt-2 px-4 flex-col items-start">
                    <p className="text-tiny uppercase font-bold">Daily Mix</p>
                    <small className="text-default-500">12 Tracks</small>
                    <h4 className="font-bold text-large">Frontend Radio</h4>
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
