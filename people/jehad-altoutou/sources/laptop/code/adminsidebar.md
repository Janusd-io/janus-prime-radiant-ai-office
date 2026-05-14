---
type: source
source_type: laptop
title: AdminSidebar
slug: adminsidebar
created: 2026-05-11
captured_by: jehad-altoutou
audience: personal
sensitivity: dept
sensitivity_confidence: 0.5
original_path: /Users/jehad/assessify/src/components/admin/AdminSidebar.tsx
original_size: 9874
original_ext: .tsx
category: code
extracted_with: code-fenced
extracted_at: "2026-05-14T09:51:33Z"
project: assessify

---

# AdminSidebar

_Extracted from `[[assessify|assessify]]/src/components/admin/AdminSidebar.tsx` on 2026-05-14._

```tsx
"use client";

import { useState, useMemo } from "react";
import Link from "next/link";
import Image from "next/image";
import { usePathname } from "next/navigation";
import { motion, AnimatePresence } from "framer-motion";
import {
  type LucideIcon,
  ChevronRight,
  LayoutDashboard,
  Users,
  FileText,
  BarChart3,
  Settings,
  Egg,
  Send,
  Code,
  ClipboardList,
  Library,
  CalendarDays,
  Briefcase,
  LayoutGrid,
  SlidersHorizontal,
} from "lucide-react";
import { LogoutButton } from "@/components/admin/LogoutButton";
import { ChangePasswordDialog } from "@/components/admin/ChangePasswordDialog";

export type NavLeaf = {
  href: string;
  label: string;
  icon: LucideIcon;
  badgeKey?: string;
};
export type NavGroup = {
  label: string;
  icon: LucideIcon;
  matchPrefix: string;
  children: NavLeaf[];
};
export type NavItem = NavLeaf | NavGroup;

function isGroup(item: NavItem): item is NavGroup {
  return "children" in item;
}

const NAV_ITEMS: NavItem[] = [
  { href: "/admin", label: "Dashboard", icon: LayoutDashboard },
  { href: "/admin/invites", label: "Invites", icon: Send },
  { href: "/admin/sessions", label: "Candidates", icon: Users },
  {
    label: "Recruitment",
    icon: Briefcase,
    matchPrefix: "/admin/recruitment",
    children: [
      { href: "/admin/recruitment", label: "Pipeline", icon: LayoutGrid },
      { href: "/admin/recruitment/candidates", label: "All candidates", icon: Users },
      { href: "/admin/recruitment/rubrics", label: "Scoring rubrics", icon: SlidersHorizontal },
    ],
  },
  { href: "/admin/assessments", label: "Assessments", icon: FileText },
  { href: "/admin/question-bank", label: "Question Bank", icon: Library },
  { href: "/admin/analytics", label: "Analytics", icon: BarChart3 },
  { href: "/admin/hr-forms", label: "HR Forms", icon: ClipboardList },
  {
    label: "Leave",
    icon: CalendarDays,
    matchPrefix: "/admin/leave-",
    children: [
      {
        href: "/admin/leave-requests",
        label: "Requests",
        icon: ClipboardList,
        badgeKey: "leaveUnread",
      },
      { href: "/admin/leave-balances", label: "Balances", icon: BarChart3 },
      { href: "/admin/team", label: "Team", icon: Users },
    ],
  },
  { href: "/admin/easter-eggs", label: "Easter Eggs", icon: Egg },
  { href: "/admin/api-docs", label: "API Docs", icon: Code },
  { href: "/admin/settings", label: "Settings", icon: Settings },
];

export function AdminSidebar({
  user,
  badges,
}: {
  user: { id: string; email: string; name: string; role: string };
  badges: Record<string, number>;
}) {
  const pathname = usePathname();

  // Auto-expand any group whose prefix matches the current path OR
  // whose children include the current page (handles cross-prefix children,
  // e.g. /admin/team nested under the /admin/leave-* group).
  const initiallyExpanded = useMemo(() => {
    const set = new Set<string>();
    for (const item of NAV_ITEMS) {
      if (!isGroup(item)) continue;
      const onPrefix = pathname.startsWith(item.matchPrefix);
      const onChild = item.children.some((c) => pathname === c.href);
      if (onPrefix || onChild) set.add(item.label);
    }
    return set;
  }, [pathname]);

  const [expanded, setExpanded] = useState<Set<string>>(initiallyExpanded);

  const toggle = (label: string) => {
    setExpanded((prev) => {
      const next = new Set(prev);
      if (next.has(label)) next.delete(label);
      else next.add(label);
      return next;
    });
  };

  return (
    <aside className="sticky top-0 hidden h-screen w-64 flex-col border-r border-zinc-200 bg-white dark:border-zinc-800 dark:bg-zinc-900 lg:flex">
      <div className="flex h-14 items-center border-b border-zinc-200 px-4 dark:border-zinc-800">
        <Link href="/admin" className="flex items-center gap-2">
          <Image
            src="/janusd-icon-200.png"
            alt="Janus Digital"
            width={28}
            height={28}
            className="shrink-0"
          />
          <span className="text-lg font-semibold tracking-tight">Assessify</span>
        </Link>
        <span className="ml-2 rounded-md bg-zinc-100 px-1.5 py-0.5 text-[10px] font-medium text-zinc-500 dark:bg-zinc-800 dark:text-zinc-400">
          Admin
        </span>
      </div>

      <nav className="flex-1 space-y-0.5 overflow-y-auto px-3 py-4">
        {NAV_ITEMS.map((item) => {
          if (!isGroup(item)) {
            return (
              <LeafLink
                key={item.href}
                item={item}
                pathname={pathname}
                badge={item.badgeKey ? badges[item.badgeKey] ?? 0 : 0}
              />
            );
          }
          const open = expanded.has(item.label);
          const childActive = item.children.some((c) => pathname === c.href);
          const onPrefix = pathname.startsWith(item.matchPrefix) || childActive;
          return (
            <div key={item.label}>
              <button
                type="button"
                onClick={() => toggle(item.label)}
                className={`group flex w-full items-center justify-between gap-3 rounded-lg px-3 py-2 text-sm font-medium transition-colors ${
                  onPrefix
                    ? "bg-zinc-100 text-zinc-900 dark:bg-zinc-800 dark:text-zinc-100"
                    : "text-zinc-600 hover:bg-zinc-100 hover:text-zinc-900 dark:text-zinc-400 dark:hover:bg-zinc-800 dark:hover:text-zinc-100"
                }`}
                aria-expanded={open}
              >
                <span className="flex items-center gap-3">
                  <item.icon className="size-4" />
                  {item.label}
                  {!open && childActive && (
                    <motion.span
                      layoutId={`nav-dot-${item.label}`}
                      className="size-1.5 rounded-full bg-blue-500"
                    />
                  )}
                </span>
                <motion.span
                  animate={{ rotate: open ? 90 : 0 }}
                  transition={{ type: "spring", stiffness: 400, damping: 30 }}
                  className="text-zinc-400"
                >
                  <ChevronRight className="size-3.5" />
                </motion.span>
              </button>
              <AnimatePresence initial={false}>
                {open && (
                  <motion.div
                    key="children"
                    initial={{ height: 0, opacity: 0 }}
                    animate={{ height: "auto", opacity: 1 }}
                    exit={{ height: 0, opacity: 0 }}
                    transition={{
                      height: { duration: 0.22, ease: [0.16, 1, 0.3, 1] },
                      opacity: { duration: 0.15, delay: 0.05 },
                    }}
                    className="overflow-hidden"
                  >
                    <div className="ml-4 mt-0.5 space-y-0.5 border-l border-zinc-200 pl-3 dark:border-zinc-800">
                      {item.children.map((child, idx) => (
                        <motion.div
                          key={child.href}
                          initial={{ opacity: 0, x: -4 }}
                          animate={{ opacity: 1, x: 0 }}
                          transition={{ delay: 0.04 + idx * 0.03, duration: 0.18 }}
                        >
                          <LeafLink item={child} pathname={pathname} badge={0} dense />
                        </motion.div>
                      ))}
                    </div>
                  </motion.div>
                )}
              </AnimatePresence>
            </div>
          );
        })}
      </nav>

      <div className="border-t border-zinc-200 px-3 py-3 dark:border-zinc-800">
        <div className="mb-2 flex items-center justify-between px-3">
          <div className="min-w-0">
            <div className="flex items-center gap-2">
              <p className="truncate text-sm font-medium">{user.name}</p>
              <span
                className={`inline-flex items-center rounded-full px-1.5 py-0.5 text-[9px] font-medium ${
                  user.role === "admin"
                    ? "bg-primary/10 text-primary"
                    : "bg-zinc-100 text-zinc-600 dark:bg-zinc-800 dark:text-zinc-400"
                }`}
              >
                {user.role === "admin" ? "Admin" : "User"}
              </span>
            </div>
            <p className="truncate text-xs text-muted-foreground">{user.email}</p>
          </div>
          <ChangePasswordDialog />
        </div>
        <LogoutButton />
      </div>
    </aside>
  );
}

function LeafLink({
  item,
  pathname,
  badge,
  dense = false,
}: {
  item: NavLeaf;
  pathname: string;
  badge: number;
  dense?: boolean;
}) {
  const active = pathname === item.href;
  return (
    <Link
      href={item.href}
      className={`relative flex items-center justify-between gap-3 rounded-lg ${
        dense ? "px-2 py-1.5" : "px-3 py-2"
      } text-sm font-medium transition-colors ${
        active
          ? "bg-zinc-100 text-zinc-900 dark:bg-zinc-800 dark:text-zinc-100"
          : "text-zinc-600 hover:bg-zinc-100 hover:text-zinc-900 dark:text-zinc-400 dark:hover:bg-zinc-800 dark:hover:text-zinc-100"
      }`}
    >
      {active && (
        <motion.span
          layoutId="nav-active-rail"
          className="absolute -left-3 top-1.5 bottom-1.5 w-0.5 rounded-r-full bg-blue-500"
          transition={{ type: "spring", stiffness: 380, damping: 30 }}
        />
      )}
      <span className="flex items-center gap-3">
        <item.icon className={dense ? "size-3.5" : "size-4"} />
        {item.label}
      </span>
      {badge > 0 && (
        <span className="inline-flex min-w-5 items-center justify-center rounded-full bg-blue-600 px-1.5 text-[10px] font-semibold text-white">
          {badge}
        </span>
      )}
    </Link>
  );
}

```