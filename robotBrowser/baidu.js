!
function (e) {
    function t(e, t, n, r, i, a, s) {
        function o() {
            g.onError && g.onError(),
                g.onEnd && g.onEnd()
        }

        function u() {
            k.request(v, b)
        }

        function c() {}

        function d(e) {
            var t = s.screen.availWidth,
                n = s.screen.availHeight,
                r = e.imData,
                i = {},
                a = [],
                o = e.xst,
                u = {
                    source: e.source,
                    url: e.url,
                    dpi: t + "x" + n,
                    xst: o,
                    pagetitle: e.pagetitle,
                    pvkey: e.pvkey,
                    appKey: e.appKey,
                    appName: e.appName,
                    cuid: e.cuid,
                    wsid: e.wsid || "",
                    ipv6: e.ipv6 || ""
                },
                c = {
                    client: u,
                    service: [],
                    f: e.f || ""
                },
                a = [],
                d = [],
                l = {
                    uid: {},
                    appid: {}
                };
            for (var f in r) {
                var m = r[f] || {},
                    p = m.imParam;
                if (p) {
                    var v = p.ucid;
                    v && !i[v] && (i[v] = 1, a.push(v));
                    var g = p.appid;
                    g && !l.appid[g] && (l.appid[g] = 1, d.push(g));
                    var y = p.imid;
                    if (!y && p.imUrl && h) {
                        var S = h.parseUrl(p.imUrl).params;
                        y = S.imid
                    }
                    c.service.push({
                        ucid: v,
                        channel: p.channel,
                        im_type: p.im_type,
                        level1: p.level1,
                        level2: p.level2,
                        level3: p.level3,
                        appid: g,
                        imid: y
                    })
                }
            }
            return {
                appidList: d,
                userIdList: a,
                entryData: c
            }
        }
        i = i || {};
        var l = i.retryDelay || 5e3,
            f = i.retryCount || 3,
            m = i.miniProgram,
            p = i.Util,
            h = new p(s),
            v = "entrySite",
            g = {};
        n && n.getCallback && (g = n.getCallback(v) || {});
        var y = null,
            S = {
                entrySite: {
                    onResult: function (e) {
                            if (0 === e.status) g.onResult && g.onResult(e),
                                g.onEnd && g.onEnd();
                            else {
                                var t = y();
                                t || o()
                            }
                        },
                        onError: function () {
                            var e = y();
                            e || o()
                        },
                        onEnd: function () {}
                }
            },
            C = d(e) || {},
            b = C.entryData,
            _ = (C.userIdList || []).join(","),
            w = (C.appidList || []).join(","),
            I = {};
        I[v] = -1 === t[v].indexOf("?") ? t[v] + "?userid=" + encodeURIComponent(_) : t[v] + "&userid=" + encodeURIComponent(_),
            I[v] += "&appid=" + encodeURIComponent(w),
            e.pvkey && (I[v] += "&pvkey=" + encodeURIComponent(e.pvkey || ""));
        var E = new r(this, S),
            k = new a({
                    miniProgram: m
                },
                I, E);
        y = function () {
                function e() {
                    return -1 !== n && t >= n ? !1 : (clearTimeout(r), r = setTimeout(function () {
                            t++,
                            k.request(v, b)
                        },
                        l), !0)
                }
                var t = 0,
                    n = f,
                    r = 0;
                return e
            }(),
            this.entry = u,
            this.onSuccess = c,
            this.destroy = function () {}
    }

    function n(e, t) {
        function n(n) {
            if (!t) return null;
            var r = t[n] || {},
                i = {
                    onResult: function () {},
                        onEnd: function () {},
                        onError: function () {}
                };
            return r.onResult && (i.onResult = function () {
                    r.onResult.apply(e, arguments)
                }),
                r.onEnd && (i.onEnd = function () {
                    r.onEnd.apply(e, arguments)
                }),
                r.onError && (i.onError = function () {
                    r.onError.apply(e, arguments)
                }),
                i
        }

        function r() {}
        e = e || this,
            this.destroy = r,
            this.getCallback = n
    }

    function r() {
        function e(e, t) {
            e && t && (a[e] = a[e] || [], a[e].push(t))
        }

        function t(e, t) {
            var n = a[e];
            if (n)
                for (var r = n.length - 1; r >= 0; r--) n[r] === t && n.splice(r, 1)
        }

        function n(e) {
            e ? a[e] = null : a = {}
        }

        function r(e) {
            return a[e]
        }

        function i(e, t) {
            var n = a[e];
            if (n)
                for (var r = 0; r < n.length; r++) n[r].apply(null, t)
        }
        var a = {};
        this.on = e,
            this.emit = i,
            this.off = t,
            this.offAll = n,
            this.getEvents = r
    }

    function i() {
        this._keyStr = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/="
    }

    function a(e, t, n, r, i, a) {
        function s() {
            if (e) {
                var t = e.getData();
                return t.aduserid
            }
        }

        function o(t) {
            var n = {
                main: {}
            };
            if (e && e.getData) {
                var r = e.getData();
                r.ssid && (n.talk = {
                            ssid: r.ssid
                        },
                        n.talk.im_type = r.imType),
                    n.main.wsid = r.wsid || ""
            }
            return t && (n.main.noHeartBeat = 1),
                n
        }

        function u() {
            return P ? !1 : (f(), P = !0, c(!0), k = setInterval(c, 1e3), !0)
        }

        function c(e) {
            if (x++, T++, e || 1e3 * T > v) {
                T = 0,
                    v = h;
                var t = !0;
                x > 15 && (x = 0, t = !1);
                var n = o(t);
                "function" == typeof g && (n = g(n)),
                    E.request(S, n)
            }
        }

        function d(e) {
            "number" == typeof e.fetchDelay && (p = e.fetchDelay)
        }

        function l() {
            v = p,
                T = 0
        }

        function f() {
            clearInterval(k),
                P = !1
        }

        function m(e, t) {
            E.addOrReplaceApi(e, t)
        }
        i = i || {};
        var p = i.fetchDelay || 1e3,
            h = i.timeoutDelay || 15e3,
            v = p,
            g = i.formatParamsFn,
            y = i.miniProgram,
            S = "fetch",
            C = s(),
            b = {};
        n && n.getCallback && (b = n.getCallback(S) || {});
        var _ = {};
        _[S] = {
            onResult: function (e) {
                    b.onResult && b.onResult(e),
                        l()
                },
                onError: function () {
                    l()
                },
                onEnd: function () {
                    l()
                }
        };
        var w = {};
        w[S] = -1 === t[S].indexOf("?") ? t[S] + "?userid=" + encodeURIComponent(C) : t[S] + "&userid=" + encodeURIComponent(C);
        var I = new r(this, _),
            E = new a({
                    miniProgram: y
                },
                w, I),
            k = 0,
            T = 0,
            P = !1,
            x = 0;
        this.isStart = function () {
                return P
            },
            this.addOrReplaceApi = m,
            this.start = u,
            this.stop = f,
            this.updateParams = d,
            this.destroy = function () {
                f()
            }
    }

    function s(e, t) {
        function n() {
            return Ct
        }

        function r(e) {
            if (St) {
                var t = {
                    type: "freetime",
                    data: e
                };
                g(t)
            }
        }

        function i(t, n, i) {
            if (St) return !1;
            if (i = i || {},
                t = t || {},
                t.imId = t.imId || t.imid, t.imid = t.imId, bt.imParam = t || {},
                bt.visitParam = n || {},
                bt.sdkOptions = i || {},
                bt.ssid = bt.visitParam.ssid || "", bt.url = i.url, void 0 === bt.sdkOptions.isSaveHistory && (bt.sdkOptions.isSaveHistory = !0), Z.addApiParams(it, {
                    wsid: n.wsid,
                    ipv6: i.ipv6
                }), st = Z.appendPageParams(st, i), !bt.ssid) {
                var a = Z.getSaveKey(bt.imParam, "ssid"),
                    s = gt.get(a);
                s && (bt.ssid = s)
            }
            dt = new L(this, ct),
                ot = new V({
                        miniProgram: U,
                        method: "GET"
                    },
                    it, dt),
                mt = new H({
                        minFreeTime: 30,
                        callback: r
                    },
                    e),
                lt = new K({
                        source: st.referrer,
                        url: st.url,
                        xst: n.xst,
                        pagetitle: st.title,
                        pvkey: n.pvKey,
                        appKey: i.appKey,
                        appName: i.appName,
                        cuid: i.cuid,
                        wsid: n.wsid,
                        f: i.f,
                        ipv6: i.ipv6,
                        imData: {
                            im: {
                                imParam: {
                                    appid: n.appid,
                                    ucid: Z.getUserId(n),
                                    channel: n.channel,
                                    im_type: t.im_type,
                                    level1: t.level1,
                                    level2: t.level2,
                                    level3: t.level3,
                                    imid: t.imid
                                }
                            }
                        }
                    },
                    it, dt, L, {
                        miniProgram: U,
                        Util: q
                    },
                    X, e),
                ft = new W(this, it, dt, L, {
                        fetchDelay: 500,
                        timeoutDelay: 1e4,
                        miniProgram: U,
                        formatParamsFn: function (e) {
                            return ft.updateParams(2 === Ct ? {
                                    fetchDelay: 1e3
                                } : {
                                    fetchDelay: 3e3
                                }),
                                e.system = e.system || {},
                                e.system.last_sys_time = et.system.lastTime || "",
                                e
                        }
                    },
                    X, e), !bt.sdkOptions.cancelEntrySite && lt && lt.entry();
            var o = "imlphistory",
                u = Z.getHistoryKey(t, n, i);
            return pt = new G({
                        maxCount: 50,
                        key: u,
                        historyStorageKey: o
                    },
                    B, e, ut),
                ht = new z({
                        key: u,
                        historyStorageKey: o,
                        getLastMessageId: function () {
                                return pt.getLastMessageId()
                            },
                            change: function (e) {
                                if (e && e.length) {
                                    var t = e[e.length - 1].message_id;
                                    pt.setLastMessageId(t),
                                        I("syncMessage", [e])
                                }
                            }
                    },
                    e, ut),
                C(),
                St = !0,
                I("init"), !0
        }

        function a(e, t) {
            return yt.on(e, t),
                this
        }

        function s(e, t) {
            return yt.off(e, t),
                this
        }

        function o(e) {
            if (St && 2 !== Ct && 1 !== Ct && !_t) {
                C(),
                    Ct = 1;
                var t = "connect",
                    n = Z.getConnectParams(bt, e);
                return ot.request(t, n),
                    this
            }
        }

        function u(e) {
            return c(e, !0)
        }

        function c(e, t) {
            if (!St) return void I("error", [{
                type: "send",
                data: e
            }]);
            var n = E() || {};
            S();
            var r = "send",
                i = Z.formatMessage(e, n);
            return t || (wt++, i.seq = wt),
                bt.sdkOptions.isSaveHistory && pt.add(i),
                t || (It["send" + i.message_id] = {
                        retry: 0,
                        data: i
                    },
                    ot.request(r, i), I("debug", [{
                        type: "send",
                        message: "send message",
                        data: i
                    }])),
                i
        }

        function d(e) {
            var t = E() || {},
                n = Z.formatMessage(e, t);
            return n
        }

        function l(e, t, n) {
            if (e) {
                var r = It["send" + e];
                if (r) {
                    var i = "send";
                    if (n !== $) return f(e),
                        void ot.request(i, r.data);
                    if (r.retry >= Y.resendCount) return void at.emit("error", [{
                        type: "send",
                        data: e,
                        result: t
                    }]);
                    S(),
                        setTimeout(function () {
                                r.retry++,
                                    ot.request(i, r.data)
                            },
                            Y.resendDelay)
                }
            }
        }

        function f(e) {
            delete et.system.list[e]
        }

        function m() {
            return et
        }

        function p(e) {
            for (var t = {},
                n = et.system,
                r = !1,
                i = 0; i < e.length; i++) {
                var a = e[i],
                    s = a.user_message_id,
                    o = parseInt(a.user_message_time, 10) || 0,
                    u = a.is_read;
                o > n.lastTime && (n.lastTime = o),
                    n.lastTime = o,
                    "0" !== n.list[s] && It["send" + s] && n.list[s] !== u && (t[s] = u, n.list[s] = u, r = !0)
            }
            return r ? t : !1
        }

        function h(e) {
            S();
            var t = "leaveWord",
                n = (rt[e.type] || "未知") + ": " + e.content,
                r = E() || {},
                i = Z.createMessageId(r.ssid, nt),
                a = {
                    ssid: r.ssid,
                    content: n,
                    source: "leaveword",
                    msgid: i
                };
            return a.message_id = i,
                a.content_type = "text",
                a.message_time = Date.now(),
                a.im_type = r.imType,
                a.imid = r.imid,
                a.seq = 0,
                ot.request(t, a),
                I("debug", [{
                    type: "leaveWord",
                    message: "leave word"
                }]),
                i
        }

        function v() {
            if (!pt) return void I("error", [{
                type: "getHistory",
                data: Y
            }]);
            var e = pt.get() || [];
            I("history", [e])
        }

        function g(e) {
            if (e || e.type) {
                var t = E() || {};
                e.im_type = t.imType,
                    e.ssid = t.ssid,
                    "object" == typeof e.data && (e.data = ut.JSON.stringify(e.data));
                var n = "userState";
                ot.request(n, e)
            }
        }

        function y(e) {
            if (e || e.type) {
                S();
                var t = E() || {};
                e.im_type = bt.imParam.im_type || 0,
                    e.ssid = t.ssid,
                    "object" == typeof e.data && (e.data = ut.JSON.stringify(e.data));
                var n = "userAction";
                ot.request(n, e)
            }
        }

        function S() {
            mt && mt.reset()
        }

        function C() {
            ft && ft.start(),
                ht && ht.start()
        }

        function b() {
            ft && ft.isStart() && ft.stop(),
                mt && mt.stop()
        }

        function _(e) {
            if (e) return e.eventName = "disconnect",
                Ct = 0,
                b(),
                delete e.key,
                void at.emit("disconnect", [e]);
            if (0 === Ct) return void b();
            var t = "disconnect",
                n = E(),
                r = {
                    im_type: n.imType,
                    ssid: n.ssid
                };
            ot.request(t, r)
        }

        function w() {
            b(),
                yt.offAll(),
                T(dt,
                    function (e) {
                        e.destroy(),
                            e = null
                    }),
                T(ot,
                    function (e) {
                        e.destroy(),
                            e = null
                    }),
                T(lt,
                    function (e) {
                        e.destroy(),
                            e = null
                    }),
                T(ft,
                    function (e) {
                        e.destroy(),
                            e = null
                    }),
                pt = null
        }

        function I(e, t) {
            if (yt.emit(e, t), "message" === e) x(t[0]);
            else if ("readData" === e) {
                var n = t[0] || {};
                for (var r in n) n.hasOwnProperty(r) && "0" === n[r] && delete It["send" + r]
            }
        }

        function E() {
            var e = bt.imParam || {},
                t = bt.visitParam || {},
                n = {
                    aduserid: Z.getUserId(t) || "",
                    ssid: bt.ssid || "",
                    imType: e.im_type || 0,
                    imid: e.imid || e.imId || "",
                    msgCount: wt,
                    wsid: t.wsid
                };
            return n
        }

        function k(e) {
            if (bt.imParam = bt.imParam || {},
                bt.visitParam = bt.visitParam || {},
                R(bt, "ssid", e.ssid), e.ssid) {
                var t = Z.getSaveKey(bt.imParam, "ssid");
                gt.save(t, e.ssid, 864e5)
            }
            R(bt.imParam, "im_type", e.imType),
                R(bt.visitParam, "aduserid", e.aduserid),
                R(bt.visitParam, "shop_id", e.shopid),
                Ct = e.connectState,
                _t = e.isForbidden
        }

        function T(e, t) {
            if (e) try {
                t(e)
            } catch (n) {}
        }

        function P() {}

        function x(e) {
            pt.add(e)
        }

        function D() {
            at.emit = I,
                at.updateData = k,
                at.disconnect = _,
                at.startFreeCheck = P,
                at.resend = l,
                at.setReadData = p,
                at.sdkInnerKey = $,
                at.stop = b,
                at.start = C,
                at.getConnectState = n
        }

        function R(e, t, n) {
            return e && t && ("number" == typeof n || n) ? (e[t] = n, e) : void 0
        }
        t = t || {};
        var O = t.sdkConfig || {},
            M = t.EventEmitter,
            A = t.isMiniProgram || !1,
            U = t.miniProgram,
            q = t.Util,
            N = t.host || O.host || "",
            H = (O.imTypes, O.defaultImType, t.FreeTimeModel),
            L = t.Callback,
            j = t.getImCallbacks,
            K = t.EntrySite,
            J = t.SdkDataModel,
            F = t.request,
            W = t.FetchData,
            B = t.StorageModel,
            G = t.HistoryModel,
            Q = t.SaveDataModel,
            z = t.SyncMessageModel,
            V = F.GetRequest,
            X = F.PostRequest,
            Z = new J(O),
            $ = (new Date).getTime().toString("16"),
            Y = {
                resendCount: 2,
                resendDelay: 1e3,
                heartDely: 12e3
            },
            et = {
                system: {
                    list: {},
                    lastTime: 0
                },
                message: {
                    list: {},
                    lastTime: 0
                }
            },
            tt = N + "/imlp/";
        Date.now || (Date.now = function () {
            return (new Date).getTime()
        });
        var nt = Date.now(),
            rt = {
                phone: "电话",
                qq: "QQ",
                email: "Email",
                wechat: "微信"
            },
            it = {
                connect: tt + "imlp/start",
                disconnect: tt + "imlp/leave",
                send: tt + "imlp/send",
                leaveWord: tt + "imlp/send",
                heartbeat: tt + "imlp/heart",
                getMessage: tt + "imlp/message",
                userState: tt + "imlp/status",
                userAction: tt + "imlp/action",
                getAsyncCard: tt + "imlp/getCardMat",
                entrySite: tt + "track/start",
                fetch: tt + "heartbeat"
            },
            at = {};
        D();
        var st = Z.getPageParams(A),
            ot = null,
            ut = new q(e),
            ct = j(at),
            dt = null,
            lt = null,
            ft = null,
            mt = null,
            pt = null,
            ht = null,
            vt = "imlp_save_base_data",
            gt = new Q(B, e, vt, ut),
            yt = new M,
            St = !1,
            Ct = 0,
            bt = {},
            _t = !1,
            wt = 0,
            It = {};
        this.init = i,
            this.on = a,
            this.off = s,
            this.connect = o,
            this.send = c,
            this.addMessage = u,
            this.leaveWord = h,
            this.reset = w,
            this.getData = E,
            this.disconnect = _,
            this.getHistory = v,
            this.resend = l,
            this.getReadData = m,
            this.setReadData = p,
            this.getConnectState = n,
            this.isInit = function () {
                return St
            },
            this.resetFreeTime = S,
            this.sendUserAction = y,
            this.sendUserState = g,
            this.stop = b,
            this.start = C,
            this.formatMessage = d
    }

    function o(e) {
        function t(e) {
            return -1 !== e.indexOf("baidu.php?url=") || -1 !== e.indexOf("link?url=") || -1 !== e.indexOf("baidu.php?sc.") ? !0 : !1
        }

        function n(e, t) {
            for (var n = new RegExp("^https?://" + t + "/imlp", "i"), r = new RegExp("^https?://" + t + "/site/[^/]+/.*", "i"), i = new RegExp("^https?://" + t + "/imsdk/page", "i"), a = [n, r, i], s = !1, o = 0; o < a.length; o++) s = s || a[o].test(e);
            return s
        }

        function r(e, t) {
            var n = new RegExp("^https?://" + t + "/imsdk/page", "i");
            return n.test(e)
        }

        function i(e) {
            var t = e.indexOf("Android") > -1 || e.indexOf("Linux") > -1,
                n = !!e.match(/\(i[^;]+;( U;)? CPU.+Mac OS X/),
                r = null;
            t ? r = "android" : n && (r = "ios");
            var i = null;
            return /(SogouMobileBrowser|SogouMSE)/i.test(e) && (i = "sogou"), {
                os: r,
                browser: i
            }
        }

        function a(e) {
            function t(e) {
                function n() {
                    var e = (y ? y + ":" : "") + "//" + v + S,
                        t = this.params;
                    if (t) {
                        var n = [];
                        for (var r in t) {
                            var i = t[r];
                            if (null !== i && void 0 !== i) {
                                var s = typeof i;
                                if ("string" !== s && "number" !== s) try {
                                    i = JSON.stringify(i)
                                } catch (o) {
                                    continue
                                }
                                n.push(r + "=" + encodeURIComponent(i))
                            }
                        }
                        n && n.length && (e += "?" + n.join("&"))
                    }
                    return a && (e += a),
                        e
                }
                var r = {};
                e = e || "";
                var i = e.indexOf("#"),
                    a = ""; - 1 !== i && (a = e.substring(i), e = e.substring(0, i));
                for (var s = e.split("?"), o = s[0], u = s[1] || "", c = u.split("&"), d = 0; d < c.length; d++) {
                    var l = c[d];
                    if (l) {
                        var f = l.split("="),
                            m = f[0],
                            p = f[1] || "";
                        try {
                            p = decodeURIComponent(p)
                        } catch (h) {
                            p = f[1] || ""
                        }
                        r[m] = p
                    }
                }
                var v = o.replace(/\?.*/, "").replace(/^(https?:)?\/\//i, "").replace(/\/.*/, ""),
                    g = v.replace(/:\d+$/, ""),
                    y = o.replace(/:?\/\/.*/, ""),
                    S = o.replace(/^(https?:)?\/\/.*?(\/|$)/i, "");
                S && (S = "/" + S),
                    this.params = r,
                    this.url = e,
                    this.removeParam = function (e) {
                        delete this.params[e],
                            this.url = n.call(this)
                    },
                    this.addParam = function (e, t) {
                        this.params[e] = t,
                            this.url = n.call(this)
                    },
                    this.getHost = function () {
                        return v
                    },
                    this.getHostname = function () {
                        return g
                    },
                    this.getProtocol = function () {
                        return y
                    },
                    this.getPathname = function () {
                        return S
                    },
                    this.removeHash = function () {
                        a = "",
                            this.url = n.call(this)
                    },
                    this.setOrigin = function (e) {
                        var r = new t(e);
                        y = r.getProtocol(),
                            g = r.getHostname(),
                            v = r.getHost(),
                            this.url = n.call(this)
                    }
            }
            return new t(e)
        }

        function s(e, t) {
            if (e && "function" == typeof t)
                for (var n = 0; n < e.length; n++) t(e[n], n)
        }

        function o(e) {
            try {
                return e()
            } catch (t) {}
        }

        function u(e, t) {
            if (!t) return e;
            if (!e) return t;
            for (var n in t) e[n] = t[n];
            return e
        }

        function c(e) {
            try {
                return JSON.parse(e)
            } catch (t) {}
        }

        function d(e) {
            try {
                return JSON.stringify(e)
            } catch (t) {}
        }

        function l(t, n) {
            e && (e.addEventListener ? e.addEventListener(t, n) : e.attachEvent && e.attachEvent("on" + t, n))
        }

        function f(e, t, n) {
            e = e || "",
                t && o(function () {
                    e = t.decode(e, n)
                });
            var r = e.split("__") || [],
                i = {
                    channel: r[0] || "",
                    level1: r[1] || "",
                    level2: r[2] || "",
                    level3: r[3] || "",
                    ucid: r[4] || "",
                    imType: r[5] || "",
                    ssid: r[6] || "",
                    appid: r[7] || ""
                };
            return i
        }

        function m(e, t, n) {
            var r = [e.channel || "", e.level1 || "", e.level2 || "", e.level3 || "", e.user_id || e.aduserid || "", e.im_type || "", e.ssid || "", e.appid || ""].join("__");
            return t && o(function () {
                    r = t.encode(r, n)
                }),
                r
        }

        function p(e, t, n) {
            var r = e || {};
            n && (r = h(r)),
                t = t || {};
            for (var i in t) {
                var a = r[i];
                a || "number" == typeof a || (r[i] = t[i])
            }
            return r
        }

        function h(e) {
            var t = d(e);
            return c(t)
        }

        function v(e) {
            e = e || "key";
            var t = (new Date).getTime().toString(16),
                n = parseInt(1e5 * Math.random()).toString(16),
                r = e + t + n;
            return r
        }

        function g(e) {
            return "undefined" === e && (e = void 0),
                e
        }

        function y(e, t) {
            var n = a(t),
                r = n.params || {},
                i = {
                    referrer: e,
                    urlParams: r,
                    pageUrl: t
                };
            return i
        }

        function S(e, t, n) {
            if (!e || "string" != typeof t) return n;
            const r = t.split(".");
            for (var i = e,
                a = 0,
                s = 0,
                o = r.length; o > s && i; s++) {
                var u = r[s];
                i = i[u],
                    a++
            }
            return (void 0 === i || null === i || a !== r.length) && (i = n),
                i
        }
        this.isMiniProgramIframe = r,
            this.createCData = m,
            this.parseCData = f,
            this.isChargeLink = t,
            this.isImlpUrl = n,
            this.getBrowser = i,
            this.parseUrl = a,
            this.eachArray = s,
            this.trycatch = o,
            this.mergeObject = u,
            this.JSON = {
                stringify: d,
                parse: c
            },
            this.bindEvent = l,
            this.jsonClone = h,
            this.mergeJson = p,
            this.createOneKey = v,
            this.filterEmptyStr = g,
            this.getPageParams = y,
            this.getValue = S
    }

    function u(e) {
        function t() {
            u || (i = 0, u = setInterval(function () {
                    i += o,
                        i >= a && i % 5 === 0 && s(i)
                },
                1e3 * o))
        }

        function n() {
            clearInterval(u),
                u = 0
        }

        function r() {
            i = 0
        }
        var i = 0,
            a = e.minFreeTime || 15,
            s = e.callback ||
            function () {},
            o = 5,
            u = 0;
        this.start = t,
            this.stop = n,
            this.reset = r
    }

    function c(e) {
        function t(t) {
            return function (n, r) {
                !n || 0 !== n.status && "0" !== n.status ? e.emit("error", [{
                    type: t,
                    data: r,
                    result: n
                }]) : e.emit(t, arguments)
            }
        }

        function n(t) {
            return function (n) {
                e.emit("error", [{
                    type: t,
                    data: n
                }])
            }
        }

        function r(t) {
            return function (n) {
                e.emit("end", [{
                    type: t,
                    data: n
                }])
            }
        }

        function i(e) {
            return {
                onResult: t(e),
                onError: n(e),
                onEnd: r(e)
            }
        }
        var a = {};
        return a.connect = {
                onResult: function (t) {
                        t = t || {};
                        var n = {
                            isForbidden: !1,
                            connectState: 0,
                            status: t.status,
                            ssid: t.ssid,
                            awake: t.awake,
                            shopid: t.shopid,
                            aduserid: t.aduserid,
                            imType: t.im_type,
                            robot: 0 === parseInt(t.robot_status, 10)
                        };
                        11 === n.status ? (e.disconnect(n, {
                                key: e.sdkInnerKey,
                                type: "cheat",
                                result: n
                            }), n.isForbidden = !0) : (0 === n.status || 2 === n.status) && (n.connectState = 2),
                            e.updateData(n),
                            0 === n.status || 2 === n.status ? (e.startFreeCheck(), e.emit("taskbegin", [n])) : e.emit("error", [{
                                type: "taskbegin",
                                data: n,
                                result: t
                            }])
                    },
                    onError: function () {
                        e.emit("error", [{
                                type: "taskbegin"
                            }]),
                            e.updateData({
                                connectState: 0
                            })
                    },
                    onEnd: r("taskbegin")
            },
            a.send = {
                onResult: function (t, n) {
                        !t || 0 !== t.status && "0" !== t.status ? n && n.msgid ? e.resend(n.msgid, t, e.sdkInnerKey) : e.emit("error", [{
                            type: "send",
                            data: null
                        }]) : e.emit("send", arguments)
                    },
                    onError: function (t) {
                        t ? e.resend(t.msgid, null, e.sdkInnerKey) : e.emit("error", [{
                            type: "send",
                            data: null
                        }])
                    },
                    onEnd: r("send")
            },
            a.leaveWord = i("leaveWord"),
            a.userState = i("userState"),
            a.userAction = i("userAction"),
            a.entrySite = i("entrySite"),
            a.fetch = {
                onResult: function (t) {
                        t = t || {},
                            t.talk = t.talk || {};
                        var n = t.talk;
                        if (11 === t.status || n && 11 === n.status, n && (void 0 !== n.switchtomanual && e.emit("switchToManual", [n.switchtomanual]), n.message instanceof Array)) {
                            if (n.kefuInput && e.emit("kefuInput", [n.kefuInput.timestamp]), t.system && t.system.message) {
                                var r = e.setReadData(t.system.message);
                                r && e.emit("readData", [r])
                            }
                            var i = d(n.message) || {},
                                a = i.messageList || [];
                            a.length && e.emit("message", [a]),
                                n.disconnect = n.disconnect || i.disconnect,
                                n.disconnect === !0 && (n.disconnect = {
                                    from: "service",
                                    result: !0
                                });
                            var s = e.getConnectState();
                            2 !== s && delete n.disconnect,
                                n.disconnect && e.disconnect(n.disconnect),
                                e.emit("fetch", arguments)
                        }
                    },
                    onError: n("fetch"),
                onEnd: r("fetch")
            },
            a.getMessage = a.fetch,
            a.disconnect = {
                onResult: function (t, n) {
                        !t || 0 !== t.status && "0" !== t.status ? e.emit("error", [{
                            type: "disconnect",
                            data: n,
                            result: t
                        }]) : (e.stop(), e.emit("disconnect", {
                            from: "client",
                            result: t,
                            data: n
                        }))
                    },
                    onError: n("disconnect"),
                onEnd: r("disconnect")
            },
            a
    }

    function d(e) {
        e = e || [];
        for (var t = {
                messageList: [],
                disconnect: null
            },
            n = 0; n < e.length; n++) {
            var r = e[n],
                i = r.content_type,
                a = r.content || {};
            "system" !== i || "cmd" !== a.type || "close" !== a.value ? t.messageList.push(r) : t.disconnect = {
                from: "service",
                result: a
            }
        }
        return t
    }

    function l(e) {
        function t() {
            var e = "abcdefghijklmnopqrstuvwxyz1234567890";
            e += e;
            var t = e.split("");
            return i(t),
                t
        }

        function n(e) {
            for (var t = [], n = _.length, i = 0; e > i; i++) {
                var a = r() % n;
                t.push(_[a])
            }
            return t.join("")
        }

        function r(e) {
            return e = e || 1e4,
                Math.round(Math.random() * e)
        }

        function i(e) {
            e.sort(function () {
                var e = r() % 2 - 1 || 1;
                return e
            })
        }

        function a(e) {
            e = e || n(32);
            var t = e.substr(-6),
                r = y();
            return t += r.toString(16).substr(-10),
                t += (r - S).toString(16),
                "m" + t
        }

        function s(e, t) {
            t = t || {};
            var n = ["wcWord", "cardId", "pt", "ac", "t"],
                r = e.imParam || {},
                i = e.visitParam || {},
                a = {};
            a = {
                    xst: i.xst || "",
                    query: i.query || "",
                    bidword: i.bidword || "",
                    city: i.city || "",
                    aduserid: i.aduserid || "",
                    level1: r.level1 || "",
                    level2: r.level2 || "",
                    level3: r.level3 || ""
                },
                a.user_id = i.user_id || "",
                a.user_id_type = i.user_id_type || "",
                a.abTest = i.abTest || "",
                a.autoConnect = i.autoConnect || 0,
                a.transparent = i.transparent || "",
                a.appid = i.appid || "",
                a.pvKey = i.pvKey || "",
                c(a, "imid", r.imId || r.imid),
                c(a, "channel", i.channel),
                c(a, "imlpAccessId", i.imlpAccessId),
                c(a, "url", i.url || e.url),
                c(a, "notifyIM", r.notifyIM),
                c(a, "cipUrl", i.cipUrl),
                c(a, "cipText", i.cipText);
            for (var s = 0; s < n.length; s++) {
                var o = n[s];
                c(a, o, t[o])
            }
            return c(a, "im_type", r.im_type, 0),
                a.ssid = e.ssid || "",
                a.params = i.params || "",
                a
        }

        function o(e) {
            var t = {};
            try {
                e || (t.url = location.href, t.referrer = document.referrer, t.title = document.title)
            } catch (n) {}
            return t
        }

        function u(e, t) {
            return t = t || {},
                e = e || {},
                c(e, "url", t.url),
                c(e, "title", t.title),
                c(e, "referrer", t.referrer),
                e
        }

        function c(e, t, n, r) {
            n || void 0 !== n && null !== n ? e[t] = n : void 0 !== r && (e[t] = r)
        }

        function d(e, t, n) {
            n = n || {};
            var r = n.historyKey,
                i = h(t) || "",
                a = e.im_type,
                s = e.imId || "",
                o = "msg" + s + a;
            return r ? "hmsg" + r : i ? "uidmsg" + i : o
        }

        function l(e, t) {
            e = e || {};
            var n = e.im_type,
                r = C[n] || b,
                i = e.imId || "",
                a = i + "_" + t;
            if ("bcp" === r.server) {
                var s = Number(e.level2) ? e.level2 : "",
                    o = Number(e.level3) ? e.level3 : "";
                a = [e.level1, s, o, n, t].join("_")
            }
            return a
        }

        function f(e, t, n) {
            var r = p(t);
            if (!r || !n) return n;
            var i = {};
            for (var a in r) e ? i[r[a]] = n[a] : i[a] = n[r[a]];
            return m(i),
                i
        }

        function m(e) {
            for (var t in e) {
                var n = e[t];
                "number" == typeof n || n || delete e[t]
            }
        }

        function p(e) {
            if ("send" === e) {
                var t = {
                    type: "content_type",
                    content: "content",
                    ssid: "ssid",
                    contenttext: "contenttext",
                    fromid: "fromid",
                    msgid: "msgid",
                    trigger: "trigger",
                    source: "source",
                    imid: "imid",
                    seq: "seq",
                    sourceTag: "source_tag"
                };
                return t.message_id = "message_id",
                    t.message_time = "message_time",
                    t.im_type = "im_type",
                    t
            }
        }

        function h(e) {
            return e = e || {},
                e.user_id || e.aduserid
        }

        function v(e, t) {
            var n = [];
            for (var r in t)(t[r] || 0 === t[r]) && n.push(r + "=" + encodeURIComponent(t[r]));
            var i = n.join("&");
            for (var r in e) e[r] += -1 === e[r].indexOf("?") ? "?" + i : "&" + i;
            return e
        }

        function g(e, t) {
            var n = "send";
            t = t || {};
            var r = t.ssid || "",
                i = t.imType || "",
                s = t.imid || "",
                o = e.msgid || e.message_id || a(r);
            e.ssid = r,
                e.source = e.source || "user",
                e.message_time = y(),
                e.msgid = o,
                e.message_id = o,
                e.im_type = i,
                e.imid = s;
            var u = p("send");
            for (var c in u) {
                var d = u[c];
                c !== d && (e[c] || 0 === e[c] || (e[c] = e[d]))
            }
            e.type = e.type || e.content_type || "text";
            var l = f(!0, n, e),
                m = l.content_type || "text";
            m += "";
            var h = C[i] || b;
            return "1" !== m || "bcp" !== h.server && "aiservice" !== h.server || (l.content_type = "text"),
                "2" === m && (l.content_type = "image"),
                l
        }

        function y() {
            return (new Date).getTime()
        }
        var S = y(),
            C = e.imTypes,
            b = e.defaultImType,
            _ = t();
        this.getConnectParams = s,
            this.createMessageId = a,
            this.getPageParams = o,
            this.getHistoryKey = d,
            this.convertInputOutputParam = f,
            this.getSaveKey = l,
            this.appendPageParams = u,
            this.getUserId = h,
            this.addApiParams = v,
            this.formatMessage = g
    }

    function f(e, t) {
        function n(e, t) {
            o && o.setItem(e, t)
        }

        function r(e) {
            return o ? o.getItem(e) : void 0
        }

        function i(e) {
            o && o.removeItem(e)
        }

        function a() {
            o && o.clear()
        }

        function s() {
            return o && o.length,
                0
        }
        var o = e.localStorage;
        t && (o = e.sessionStorage),
            this.setItem = n,
            this.getItem = r,
            this.removeItem = i,
            this.clear = a,
            this.length = s
    }

    function m(e, t, n, r) {
        function i(e, t) {
            if (e) {
                var n = e.msgList;
                if (t instanceof Array) {
                    for (var r = 0; r < t.length; r++) n.push(t[r]);
                    o = t[t.length - 1].message_id
                } else n.push(t),
                    o = t.message_id; - 1 !== c && c > 0 && n.length > c && n.splice(0, n.length - c),
                    e.updateTime = (new Date).getTime()
            }
        }

        function a(e) {
            try {
                var t = r.JSON.stringify(e);
                u.setItem(l, t)
            } catch (n) {
                "QuotaExceededError" === n.name || 22 === n.code
            }
        }

        function s() {
            var e = null;
            try {
                e = u.getItem(l)
            } catch (t) {}
            if (e) try {
                e = r.JSON.parse(e)
            } catch (t) {}
            return e = e || {}
        }
        var o = null,
            u = new t(n),
            c = e.maxCount || 50,
            d = e.key,
            l = e.historyStorageKey;
        this.get = function () {
                var e = s(),
                    t = null,
                    n = e[d];
                return n && (t = n.msgList || [], n.updateTime = (new Date).getTime()),
                    t && (o = t[t.length - 1].message_id),
                    t
            },
            this.add = function (e) {
                var t = s();
                t[d] = t[d] || {};
                var n = t[d];
                n.msgList = n.msgList || [],
                    i(n, e),
                    a(t)
            },
            this.getLastMessageId = function () {
                return o
            },
            this.setLastMessageId = function (e) {
                o = e
            },
            this.remove = function () {
                var e = s(),
                    t = e[d];
                t && (delete e[d], a(e))
            },
            this.changeKey = function (e) {
                var t = s(),
                    n = t[d];
                n && (t[e] = t[d], t[e].updateTime = (new Date).getTime(), delete t[d], a(t)),
                    d = e
            }
    }

    function p(e, t, n, r) {
        function i(e) {
            return e ? l : d
        }

        function a(e) {
            var t = i(e),
                a = t.getItem(n),
                s = r.JSON.parse(a) || {};
            s = u(s);
            var o = r.JSON.stringify(s);
            return t.setItem(n, o),
                s
        }

        function s(e, t, s, o) {
            var u = i(o),
                c = a(o) || {},
                d = 0;
            s && (d = s + (new Date).getTime()),
                c[e] = {
                    timestamp: d,
                    data: t
                };
            var l = r.JSON.stringify(c);
            u.setItem(n, l)
        }

        function o(e, t) {
            var n = a(t) || {},
                r = n[e] || {};
            return r.data
        }

        function u(e) {
            if (e) {
                var t = (new Date).getTime();
                for (var n in e) {
                    var r = e[n];
                    c(r, t) && delete e[n]
                }
                return e
            }
        }

        function c(e, t) {
            return t = t || (new Date).getTime(),
                e.timestamp && e.timestamp < t ? !0 : !1
        }
        var d = new e(t),
            l = new e(t, !0);
        this.save = s,
            this.get = o
    }

    function h(e, t, n) {
        function r(e) {
            if (e = e || t.event, e && e.key === c) {
                var r = n.JSON.parse(e.newValue) || {};
                if (r[u]) {
                    var i = r[u].msgList;
                    if (i && i.length) {
                        for (var a = l(), s = [], o = !1, f = 0; f < i.length; f++) {
                            var m = i[f];
                            m.message_id !== a ? o && s.push(m) : o = !0
                        }
                        o || (s = i),
                            s && s.length && d(s)
                    }
                }
            }
        }

        function i() {
            o || (o = !0, n.bindEvent("storage", r))
        }

        function a() {
            o = !1
        }

        function s() {
            a()
        }
        var o = !1,
            u = e.key,
            c = e.historyStorageKey,
            d = e.change ||
            function () {},
            l = e.getLastMessageId ||
            function () {};
        this.start = i,
            this.stop = a,
            this.destroy = s
    }

    function v() {
        this.request = function () {},
            this.startHeartbeat = function () {},
            this.stopHeartbeat = function () {},
            this.destroy = function () {
                this.stopHeartbeat()
            },
            this.addOrReplaceApi = function () {}
    }

    function g(e) {
        function t() {}

        function n(t) {
            if (!t) return "";
            if ("POST" === i && "json" === e.contentType) return JSON.stringify(t);
            var n = [];
            for (var r in t) {
                var a = t[r];
                "number" == typeof a ? n.push(r + "=" + a) : a && "object" == typeof a ? n.push(r + "=" + encodeURIComponent(JSON.stringify(a))) : a && "string" == typeof a && n.push(r + "=" + encodeURIComponent(a))
            }
            return n.join("&")
        }

        function r(e) {
            if (e)
                for (var t in e) e.hasOwnProperty(t) && m.setRequestHeader(t, e[t] || "")
        }
        var i = (e.type || "GET").toUpperCase(),
            a = e.url,
            s = e.data,
            o = "application/x-www-form-urlencoded",
            u = e.dataType;
        "json" === e.contentType && (o = "application/json");
        var c = e.error || t,
            d = e.success || t,
            l = e.complete || t;
        if (!a) return c(),
            void l();
        var f = n(s);
        "GET" === i && f && (a += -1 === a.indexOf("?") ? "?" + f : "&" + f);
        var m = new XMLHttpRequest;
        m.open(i, a, !0),
            m.setRequestHeader("Content-Type", o),
            r(e.headers),
            m.onreadystatechange = function () {
                if (4 === m.readyState) {
                    if (m.status >= 200 && m.status < 300 || 304 === m.status) {
                        var e = m.responseText;
                        try {
                            "json" === u && (e = JSON.parse(e)),
                                d(e, m.status, m)
                        } catch (t) {
                            c()
                        }
                    } else c();
                    l(m, m.status)
                }
            },
            "POST" === i && f ? m.send(f) : m.send()
    }

    function y(e, t, n) {
        function r(e, r) {
            var a = t[e],
                s = n.getCallback(e);
            try {
                g({
                    type: "post",
                    url: a,
                    data: r,
                    dataType: "json",
                    contentType: "json",
                    success: function (e) {
                            s.onResult && !i && s.onResult(e)
                        },
                        error: function () {
                            s.onError && !i && s.onError()
                        },
                        complete: function () {
                            s.onEnd && !i && s.onEnd()
                        }
                })
            } catch (o) {}
        }
        var i = !1;
        this.destroy = function () {
                i = !0
            },
            this.addOrReplaceApi = function (e, n) {
                t = t || {},
                    t[e] = n
            },
            this.request = r
    }

    function v() {
        this.request = function () {},
            this.startHeartbeat = function () {},
            this.stopHeartbeat = function () {},
            this.destroy = function () {
                this.stopHeartbeat()
            },
            this.addOrReplaceApi = function () {}
    }

    function S(t, n, r, i) {
        function a() {
            document.getElementsByTagName("head")[0].removeChild(p),
                i.onEnd && i.onEnd(n)
        }

        function s(e, t, n) {
            e && (e.addEventListener ? e.addEventListener(t, n) : e.attachEvent ? e.attachEvent("on" + t, n) : e["on" + t] = n)
        }
        if (t && n) {
            i = i || {},
                r = r ||
                function () {};
            var o = "bcpsdk_" + encodeURIComponent(t.replace(/.*\//, "").replace(/\?.*/, ""));
            e[o] = r,
                n.callback = encodeURIComponent(o),
                n.t = (new Date).getTime();
            var u = [],
                c = Object.prototype.toString;
            for (var d in n) {
                var l, f = "";
                if ("number" == typeof n[d] && (f = 0), "[object Object]" === c.call(n[d])) {
                    try {
                        l = JSON.stringify(n[d])
                    } catch (m) {
                        l = "{}"
                    }
                    u.push(d + "=" + encodeURIComponent(l))
                } else u.push(d + "=" + encodeURIComponent(n[d] || f))
            }
            delete n.callback,
                u = u.join("&"),
                t += -1 !== t.indexOf("?") ? "&" + u : "?" + u;
            var p = document.createElement("script");
            p.setAttribute("async", "true"),
                s(p, "load", a),
                s(p, "error",
                    function () {
                        document.getElementsByTagName("head")[0].removeChild(p),
                            i.onError && i.onError(n)
                    }),
                document.getElementsByTagName("head")[0].appendChild(p),
                p.src = t
        }
    }

    function C(t, n, r) {
        function i(e, t) {
            var i = n[e],
                a = r.getCallback(e);
            S(i, t,
                function (e) {
                    a.onResult && !d && a.onResult(e, t)
                }, {
                    onError: function () {
                            d || a.onError(t)
                        },
                        onEnd: function () {
                            d || a.onEnd(t)
                        }
                })
        }

        function a(t, n) {
            c = e.setInterval(function () {
                    i(t, n)
                },
                u)
        }

        function s() {
            e.clearInterval(c)
        }
        var o = t || {},
            u = o.heartDely || 6e3,
            c = 0,
            d = !1;
        this.destroy = function () {
                s(),
                    d = !0
            },
            this.startHeartbeat = a,
            this.stopHeartbeat = s,
            this.request = i
    }

    function b(e, t, n) {
        return t ? t[e].apply(t, n) : void 0
    }

    function _(e, t) {
        t[e] = function () {
            return b(e, k, arguments)
        }
    }
    if (!e.BcpSdk) {
        try {
            module.exports = t
        } catch (w) {}
        try {
            module.exports = n
        } catch (w) {}
        try {
            module.exports = r
        } catch (w) {}
        i.prototype.encode = function (e, t) {
                t = t || this._keyStr;
                var n, r, i, a, s, o, u, c = "",
                    d = 0;
                for (e = this._utf8_encode(e); d < e.length;) n = e.charCodeAt(d++),
                    r = e.charCodeAt(d++),
                    i = e.charCodeAt(d++),
                    a = n >> 2,
                    s = (3 & n) << 4 | r >> 4,
                    o = (15 & r) << 2 | i >> 6,
                    u = 63 & i,
                    isNaN(r) ? o = u = 64 : isNaN(i) && (u = 64),
                    c = c + t.charAt(a) + t.charAt(s) + t.charAt(o) + t.charAt(u);
                return c
            },
            i.prototype.decode = function (e, t) {
                t = t || this._keyStr;
                var n, r, i, a, s, o, u, c = "",
                    d = 0;
                for (e = e.replace(/[^A-Za-z0-9\+\/\=]/g, ""); d < e.length;) a = t.indexOf(e.charAt(d++)),
                    s = t.indexOf(e.charAt(d++)),
                    o = t.indexOf(e.charAt(d++)),
                    u = t.indexOf(e.charAt(d++)),
                    n = a << 2 | s >> 4,
                    r = (15 & s) << 4 | o >> 2,
                    i = (3 & o) << 6 | u,
                    c += String.fromCharCode(n),
                    64 !== o && (c += String.fromCharCode(r)),
                    64 !== u && (c += String.fromCharCode(i));
                return c = this._utf8_decode(c)
            },
            i.prototype._utf8_encode = function (e) {
                e = e.replace(/\r\n/g, "\n");
                for (var t = "",
                    n = 0; n < e.length; n++) {
                    var r = e.charCodeAt(n);
                    128 > r ? t += String.fromCharCode(r) : r > 127 && 2048 > r ? (t += String.fromCharCode(r >> 6 | 192), t += String.fromCharCode(63 & r | 128)) : (t += String.fromCharCode(r >> 12 | 224), t += String.fromCharCode(r >> 6 & 63 | 128), t += String.fromCharCode(63 & r | 128))
                }
                return t
            },
            i.prototype._utf8_decode = function (e) {
                for (var t = "",
                    n = 0,
                    r = 0,
                    i = 0,
                    a = 0; n < e.length;) r = e.charCodeAt(n),
                    128 > r ? (t += String.fromCharCode(r), n++) : r > 191 && 224 > r ? (i = e.charCodeAt(n + 1), t += String.fromCharCode((31 & r) << 6 | 63 & i), n += 2) : (i = e.charCodeAt(n + 1), a = e.charCodeAt(n + 2), t += String.fromCharCode((15 & r) << 12 | (63 & i) << 6 | 63 & a), n += 3);
                return t
            };
        try {
            module.exports = i
        } catch (w) {}
        try {
            module.exports = a
        } catch (w) {}
        try {
            module.exports = s
        } catch (w) {}
        try {
            module.exports = o
        } catch (w) {}
        try {
            module.exports = u
        } catch (w) {}
        try {
            module.exports = c
        } catch (w) {}
        try {
            module.exports = l
        } catch (w) {}
        try {
            module.exports = f
        } catch (w) {}
        try {
            module.exports = m
        } catch (w) {}
        try {
            module.exports = p
        } catch (w) {}
        try {
            module.exports = h
        } catch (w) {}
        y.prototype = new v,
            y.prototype.constructor = y,
            C.prototype = new v,
            C.prototype.constructor = C;
        var I = {
            imlpApp: {
                appid: "wx2fde1496e4d81009",
                path: ""
            },
            host: "https://ada.baidu.com",
            defaultImType: {
                name: "default",
                server: "bcp"
            },
            clientSdkDataTimeout: 432e5
        };
        !
        function (e) {
            var t = [];
            t[0] = {
                    name: "商桥",
                    server: "bcp"
                },
                t[1] = {
                    name: "商务通",
                    server: "bcp"
                },
                t[2] = {
                    name: "53客服",
                    server: "bcp"
                },
                t[3] = {
                    name: "快商通",
                    server: "bcp"
                },
                t[4] = {
                    name: "ai客服",
                    server: "aiservice"
                },
                t[5] = {
                    name: "咨询分诊",
                    server: "guide"
                },
                t[6] = {
                    name: "乐语",
                    server: "bcp"
                },
                t[7] = {
                    name: "美洽",
                    server: "bcp"
                },
                t[8] = {
                    name: "易聊通",
                    server: "bcp"
                },
                t[9] = {
                    name: "螳螂",
                    server: "bcp"
                },
                t[10] = {
                    name: "鱼塘",
                    server: "bcp"
                },
                t[11] = {
                    name: "live800",
                    server: "bcp"
                },
                t[12] = {
                    name: "小能",
                    server: "bcp"
                },
                t[10001] = {
                    name: "熊掌号",
                    server: "bcp"
                },
                e.imTypes = t
        }(I);
        try {
            module.exports = I
        } catch (w) {}
        for (var E = ["init", "on", "connect", "send", "leaveWord", "reset", "getData", "disconnect", "getHistory", "resend", "getConnectState", "isInit", "resetFreeTime", "sendUserAction", "sendUserState"], k = null, T = {},
            P = 0; P < E.length; P++) {
            var x = E[P];
            _(x, T)
        }
        T.init = function (i, d, v) {
                return k = new s(e, {
                        EventEmitter: r,
                        FreeTimeModel: u,
                        getImCallbacks: c,
                        Callback: n,
                        Util: o,
                        EntrySite: t,
                        SdkDataModel: l,
                        StorageModel: f,
                        HistoryModel: m,
                        SaveDataModel: p,
                        SyncMessageModel: h,
                        request: {
                            GetRequest: C,
                            PostRequest: y
                        },
                        sdkConfig: I,
                        FetchData: a,
                        host: v.host
                    }),
                    k.init(i, d, v)
            },
            e.BcpSdk = T
    }
}(window);