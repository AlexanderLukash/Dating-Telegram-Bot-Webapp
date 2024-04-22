'use client'
import React, {useEffect, useState} from "react";
import {BackEnd_URL} from "@/config/url";
import {Button} from "@nextui-org/button";
import {HeartIconFill} from "@/components/HeartIconFill";
import {HeartIcon} from "@/components/HeartIcon";
import {getUserLike} from "@/components/api";
import {Spinner} from "@nextui-org/spinner";


// @ts-ignore
export const LikeButton = ({from_user_id, to_user_id}) => {

    const [liked, setLiked] = useState(false);
    useEffect(() => {
        const fetchData = async () => {
            try {
                const get_like = await getUserLike(from_user_id, to_user_id); // Получаем данные лайка
                setLiked(!!get_like.data); // Устанавливаем состояние в зависимости от наличия лайка
            } catch (error) {
                console.error('Ошибка при получении данных лайка:', error);
            }
        };

        fetchData(); // Вызываем асинхронную функцию для получения данных лайка
    }, [from_user_id, to_user_id]);

    const [showSpinner, setShowSpinner] = useState(true);

    useEffect(() => {
        const timer = setTimeout(() => {
            setShowSpinner(false);
        }, 400); // Показываем спиннер в течение 2 секунд

        return () => clearTimeout(timer);
    }, []); // Пустой массив зависимостей, чтобы эффект запустился только один разl

    const handleLikeClick = () => {
        const updatedLiked = !liked; // Сохраняем обновленное значение liked

        setLiked(updatedLiked); // Обновляем состояние liked

        const likeEndpoint = updatedLiked
            ? `${BackEnd_URL}/likes/add/${from_user_id}/${to_user_id}`
            : `${BackEnd_URL}/likes/remove/${from_user_id}/${to_user_id}`;

        fetch(likeEndpoint, {
            method: updatedLiked ? 'POST' : 'DELETE',
            headers: {
                'bypass-tunnel-reminder': 'true',
                'User-Agent': 'Custom',
                'ngrok-skip-browser-warning': 'true'
            }
        })
            .then((res) => {
                // Обработка успешного ответа
            })
            .catch((error) => {
                console.error('Ошибка при отправке лайка:', error);
                // Можно добавить логику обработки ошибки здесь
            });
    };


    // @ts-ignore
    return (
        <>
            {showSpinner ? (
                <Spinner
                    color={"danger"}
                    size={"sm"}
                    labelColor="danger"
                />
            ) : (
                <Button
                    isIconOnly
                    color="danger"
                    variant="faded"
                    aria-label="Like"
                    className="float-right"
                    onClick={handleLikeClick}
                >
                    {liked ? (
                        <HeartIconFill filled={undefined} size={undefined} height={undefined} width={undefined}
                                       label={undefined}/>
                    ) : (
                        <HeartIcon filled={undefined} size={undefined} height={undefined} width={undefined}
                                   label={undefined}/>
                    )}
                </Button>
            )}
        </>
    );
};