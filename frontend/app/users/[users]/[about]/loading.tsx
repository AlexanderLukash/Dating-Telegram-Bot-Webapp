import React from "react";
import {Spinner} from "@nextui-org/spinner";

export default function Loading() {
    return (
        <div className="flex flex-col items-center justify-center w-full h-screen">
            <Spinner color="danger" labelColor="danger"/>
        </div>
    );
}