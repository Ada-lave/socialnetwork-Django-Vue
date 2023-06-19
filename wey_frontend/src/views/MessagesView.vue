<template>
    <div class="max-w-7xl mx-auto grid grid-cols-4 gap-4">
        <div class="main-left col-span-1">
            <div class="p-4 bg-white border border-gray-200 rounded-lg">

                <div class="space-y-4">
                    

                     <div class="flex items-center justify-between">

                        <div class="flex items-center space-x-2">
                        <img src="https://i.pravatar.cc/300?img=70" class="w-[40px] rounded-full">

                        <p class="text-xs"> Your Friend </p>
                        <p class="text-gray-500 text-xs">19 минут назад</p>

                        </div>

                        
                    </div>
                   

                </div>
            </div>
        </div>

        <div class="main-center col-span-3 space-y-4">

            <div class="bg-white border border-gray-200 rounded-lg">
                <div class="flex flex-col flex-grow p-4">
                    <div class="flex w-full mt-2 space-x-3 max-w-md ml-auto justify-end">
                        <div>
                            <div class="bg-blue-600 text-white p-3 rounded-l-lg rounded-br-lg">
                                <p class="text-sm"> Какое-то сообщение написанное кем-то </p>
                            </div>

                            <span class="text-xs text-gray-400 leading-none">3 минуты назад</span>
                        </div>

                        <div class="flex-shrink-0 h-10 w-10 rounded-full bg-gray-200">

                            <img src="https://i.pravatar.cc/300?img=70" class="w-[40px] rounded-full">

                        </div>
                    </div>

                    <div class="flex w-full mt-2 space-x-3 max-w-md mr-auto justify-start">
                        <div class="flex-shrink-0 h-10 w-10 rounded-full bg-gray-200">

                            <img src="https://i.pravatar.cc/300?img=70" class="w-[40px] rounded-full">

                        </div>
                        <div>
                            <div class="bg-gray-200 p-3 rounded-l-lg rounded-br-lg">
                                <p class="text-sm"> Какое-то сообщение написанное кем-то </p>
                            </div>

                            <span class="text-xs text-gray-400 leading-none">3 минуты назад</span>
                        </div>

                        
                    </div>

                    
                </div>

                
            </div>

            <div class="bg-white border border-gray-200 rounded-lg">
               
               <div class="p-4">
                   <textarea class="p-4 w-full bg-gray-100 rounded-lg" placeholder=""></textarea>
               </div>

               <div class="p-4 border-t border-gray-100 flex justify-between">


                   <a class="ml-auto py-4 px-3 bg-purple-600 text-white rounded-lg ">Отправить</a>

               </div>
           </div>
        </div>
    </div>
</template>