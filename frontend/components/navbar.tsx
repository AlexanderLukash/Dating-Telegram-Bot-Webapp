import {
    Navbar as NextUINavbar,
    NavbarContent,
    NavbarMenu,
    NavbarMenuToggle,
    NavbarBrand,
    NavbarItem,
    NavbarMenuItem,
} from "@nextui-org/navbar";
import {Button} from "@nextui-org/button";
import {Kbd} from "@nextui-org/kbd";
import {Link} from "@nextui-org/link";
import {Input} from "@nextui-org/input";

import {link as linkStyles} from "@nextui-org/theme";

import {siteConfig} from "@/config/site";
import NextLink from "next/link";
import clsx from "clsx";

import {ThemeSwitch} from "@/components/theme-switch";
import {
    TwitterIcon,
    GithubIcon,
    DiscordIcon,
    HeartFilledIcon,
    SearchIcon,
} from "@/components/icons";

import {Logo} from "@/components/icons";

export const Navbar = () => {
    const searchInput = (
        <Input
            aria-label="Search"
            classNames={{
                inputWrapper: "bg-default-100",
                input: "text-sm",
            }}
            endContent={
                <Kbd className="hidden lg:inline-block" keys={["command"]}>
                    K
                </Kbd>
            }
            labelPlacement="outside"
            placeholder="Search..."
            startContent={
                <SearchIcon className="text-base text-default-400 pointer-events-none flex-shrink-0"/>
            }
            type="search"
        />
    );

    return (
        <NextUINavbar maxWidth="xl" position="sticky">
            <NavbarContent className="basis-1/5 sm:basis-full" justify="start">
                <NavbarBrand as="li" className="gap-3 max-w-fit">
                    <NextLink className="flex justify-start items-center gap-1" href="/">
                        <Logo/>
                        <p className="font-bold text-inherit">Dating WebApp</p>
                    </NextLink>
                </NavbarBrand>
            </NavbarContent>

            <NavbarContent
                className="hidden sm:flex basis-1/5 sm:basis-full"
                justify="end"
            >
                <NavbarItem className="hidden sm:flex gap-2">
                    <ThemeSwitch/>
                </NavbarItem>
            </NavbarContent>

            <NavbarContent className="sm:hidden basis-1 pl-4" justify="end">
                <ThemeSwitch/>
            </NavbarContent>
        </NextUINavbar>
    );
};
