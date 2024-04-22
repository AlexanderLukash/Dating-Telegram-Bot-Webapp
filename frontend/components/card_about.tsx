'use client'
import {Card, CardBody, CardFooter, CardHeader} from "@nextui-org/card";
import {Image} from "@nextui-org/image";
import {Button} from "@nextui-org/button";
import {Link} from "@nextui-org/link";
import React, {Suspense} from "react";
import {motion} from "framer-motion";
import Loading from "@/app/users/[users]/[about]/loading";
import {LikeButton} from "@/components/LikeButton";
import {HeartIconFill} from "@/components/HeartIconFill";
import {HeartIcon} from "@/components/HeartIcon";


export const CardAboutUser = ({data, params, index}: { data: any, params: any, index: number }) => {
    return (
        <motion.div
            initial={{x: -100, opacity: 0}}
            animate={{x: 0, opacity: 1}}
            transition={{duration: 0.5, delay: index * 0.2}}
        >
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
                    <Suspense fallback={<Loading/>}>
                        <LikeButton from_user_id={params.users} to_user_id={data.data.telegram_id}/>
                    </Suspense>
                </CardHeader>
                <CardBody className="overflow-visible py-2 items-center justify-center">
                    <Image
                        isZoomed
                        isBlurred
                        alt="Card background"
                        className="object-cover rounded-xl items-center justify-center max-h-96"
                        src={data.data.photo} // Використовуйте фото з API
                        width={270}
                    />
                </CardBody>
                {data.data.about !== 'NULL' && (
                    <CardFooter>
                        <p className="text-small font-semibold text-default-400">
                            {data.data.about}
                        </p>
                    </CardFooter>
                )}
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
        </motion.div>
    )
}