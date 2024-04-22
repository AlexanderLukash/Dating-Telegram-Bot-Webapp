import {Suspense} from "react";
import Loading from "@/app/users/[users]/[about]/loading";


export default function AboutLayout({
										children,
									}: {
	children: React.ReactNode;
}) {
	return (
		<section className="flex flex-col items-center justify-center gap-4 py-8 md:py-10 -mt-20">
			<div className="inline-block max-w-lg text-center justify-center">
				<Suspense fallback={<Loading/>}>
					{children}
				</Suspense>
			</div>
		</section>
	);
}