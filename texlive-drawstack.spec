%global tl_name drawstack
%global tl_revision 28582

Name:		texlive-%{tl_name}
Version:	%{tl_revision}
Release:	1
Summary:	Draw execution stacks
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/drawstack
License:	lppl1.3
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/drawstack.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/drawstack.doc.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
This simple LaTeX package provides support for drawing execution stack
(typically to illustrate assembly language notions). The code is written
on top of TikZ.

