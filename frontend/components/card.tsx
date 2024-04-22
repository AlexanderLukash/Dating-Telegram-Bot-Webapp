'use client'
import {Card, CardBody, CardFooter, CardHeader} from "@nextui-org/card";
import {Image} from "@nextui-org/image";
import {Button} from "@nextui-org/button";
import {Link} from "@nextui-org/link";
import React from "react";
import {motion} from "framer-motion";


export const CardUser = ({user, param, index}: { user: any, param: any, index: number }) => {
    return (
        <motion.div
            initial={{x: -100, opacity: 0}}
            animate={{x: 0, opacity: 1}}
            transition={{duration: 0.5, delay: index * 0.2}}
        >
            <Card className="py-4 mb-4">
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
                        className="object-cover rounded-xl items-center justify-center max-h-96"
                        src={user.photo} // Використовуйте фото з API
                        width={270}
                    />
                </CardBody>
                <CardFooter className="gap-3 -mt-2 -mb-2 px-3 py-0 text-small text-default-400">
                    <Button
                        href={`/users/${param.users}/${user.telegram_id}`}
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
        </motion.div>
    )
}